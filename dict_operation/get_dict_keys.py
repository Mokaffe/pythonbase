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
    # for item in secrets:
    #     key = item['data']
    #     print(key)
    #     for key, value in item['data'].items():
    #         data_dict_keys.append(key)
    #
    # print(data_dict_keys)

    # 简单推导的方法获取key
    print([key for secret in secrets for key in secret.get('data')])
    for secret in secrets:
        for key in secret.get('data'):
            data_dict_keys.append(key)

    print(data_dict_keys)

    env = {'a': 'aaa', 'b': 'bbb', 'c': 'ccc'}
    k = []
    for key in env:
        print(key)
        k.append(key)
    print(k)

    # dict 的方法 dict_object.keys() 也可以得到所有的keys
