if __name__ == '__main__':
    # d = {}
    # d.setdefault('name')
    # # {'name': None}
    # print(d)
    #
    # d.setdefault('name', 'hello')
    # # {'name': None}
    # print(d)
    #
    # d.setdefault('name_1', 'world')
    # # {'name': None, 'name_1': 'world'}
    # print(d)
    #
    # print(d.setdefault('name_1', 'sss'))
    #
    # d['name_1'] = 'value'
    # print(d.setdefault('name_1', 'a'))
    # print(d)
    #
    # girls = ['alice', 'bernice', 'clarice']
    # boys = ['chris', 'arnold', 'bob']
    #
    # letterGirls = {}
    #
    # for girl in girls:
    #     letterGirls.setdefault(girl[0], []).append(girl)
    #
    # print([b + '+' + g for b in boys for g in letterGirls[b[0]]])

    env = {
        "NAME": "hbao",
        "secret": ["ABCENV", 'sss']
    }

    if env and 'secret' in env:
        print(env.get('secret'))
