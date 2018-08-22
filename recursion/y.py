import yaml


def generate_yaml(agent_image):
    config_map = yaml.load(CONFIG_MAP % {
        'agent_image': agent_image
    })
    return config_map


CONFIG_MAP = '''
apiVersion: v1
kind: ConfigMap
metadata:
  labels:
    app: gocd
data:
  preconfigure_server.sh: |-
    #!/bin/bash

    SERVICE_ACCOUNT_PATH=/var/run/secrets/kubernetes.io/serviceaccount
    KUBE_TOKEN=$(<${SERVICE_ACCOUNT_PATH}/token)

    while true
    do
      status_code=$(curl "http://localhost:8153/go/api/v1/health" -o /dev/null -w "%{http_code}")
      if [ $status_code == 200 ]; then
        break
      fi
      sleep 10
    done

    set -e

    (curl --fail -i "http://localhost:8153/go/api/elastic/profiles" \
      -H "Accept: application/vnd.go.cd.v1+json" \
      -H "Content-Type: application/json" \
      -X POST -d "{
        "id": "demo-app",
        "plugin_id": "cd.go.contrib.elasticagent.kubernetes",
        "properties": [
          {
            "key": "Image",
            "value": %(agent_image)s
          },
          {
            "key": "PodConfiguration",
            "value": "apiVersion: v1\nkind: Pod\nmetadata:\n  name: pod-name-prefix-{\{ POD_POSTFIX }\}\n  labels:\n    app: web\nspec:\n  containers:\n    - name: gocd-agent-container-{\{ CONTAINER_POSTFIX \}}\n      image: '{{ GOCD_AGENT_IMAGE }}:{{ LATEST_VERSION }}'\n      securityContext:\n        privileged: true"
          },
          {
            "key": "SpecifiedUsingPodConfiguration",
            "value": "false"
          },
          {
            "key": "Privileged",
            "value": "true"
          }
        ]
      }" >> /godata/logs/preconfigure.log)

    echo "Trying to configure plugin settings." >> /godata/logs/preconfigure.log

    (curl --fail -i "http://localhost:8153/go/api/admin/plugin_settings" \
      -H "Accept: application/vnd.go.cd.v1+json" \
      -H "Content-Type: application/json" \
      -X POST -d "{
        "plugin_id": "cd.go.contrib.elasticagent.kubernetes",
        "configuration": [
          {
            "key": "go_server_url",
            "value": "https://gocd-server:8154/go"
          },
          {
            "key": "kubernetes_cluster_url",
            "value": "https://"$KUBERNETES_SERVICE_HOST":"$KUBERNETES_SERVICE_PORT_HTTPS""
          },
          {
            "key": "namespace",
            "value": "default"
          },
          {
            "key": "security_token",
            "value": ""$KUBE_TOKEN""
          }
        ]
      }" >> /godata/logs/preconfigure.log)

    echo "Trying to creating a hello world pipeline." >> /godata/logs/preconfigure.log

    (curl --fail -i "http://localhost:8153/go/api/admin/pipelines" \
      -H "Accept: application/vnd.go.cd.v5+json" \
      -H "Content-Type: application/json" \
      -X POST -d "{ "group": "sample",
                    "pipeline": {
                      "label_template": "${COUNT}",
                      "name": "hello_world",
                      "materials": [
                        {
                          "type": "git",
                          "attributes": {
                            "url": "https://github.com/gocd-contrib/getting-started-repo",
                            "shallow_clone": true
                          }
                        }
                      ],
                      "stages": [
                        {
                          "name": "default_stage",
                          "jobs": [
                            {
                              "name": "default_job",
                              "elastic_profile_id": "demo-app",
                              "tasks": [
                                {
                                  "type": "exec",
                                  "attributes": {
                                    "command": "echo",
                                    "arguments": [
                                      "Hello World"
                                    ]
                                  }
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  }" >> /godata/logs/preconfigure.log )

    echo "Unpausing the pipeline." >> /godata/logs/preconfigure.log

    (curl --fail -i "http://localhost:8153/go/api/pipelines/hello_world/unpause" \
           -H "Accept: application/vnd.go.cd.v1+json" \
           -H "X-GoCD-Confirm: true" \
           -X POST >> /godata/logs/preconfigure.log)

    echo "Done preconfiguring the GoCD server" > /godata/logs/preconfigure_complete.log
'''
