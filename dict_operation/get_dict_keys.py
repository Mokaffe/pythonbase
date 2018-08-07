secrets = [
    {
        "metadata": {
            "name": "hbao-secret-secret1",
            "namespace": "default",
            "labels": {
                "planet": "hbao"
            }
        },
        "data": {
            "secret1": "dGhpcyBpcyBzZWNyZXQgMQ=="
        }
    },
    {
        "metadata": {
            "name": "hbao-secret-secret2",
            "namespace": "default",
            "labels": {
                "planet": "hbao"
            }
        },
        "data": {
            "secret2": "dGhpcyBpcyBzZWNyZXQgMg=="
        }
    }
]

if __name__ == '__main__':
    data_dict_keys = []
    for item in secrets:
        key = item['data']
        print(key)
        for key, value in item['data'].items():
            data_dict_keys.append(key)

    print(data_dict_keys)
