import json

if __name__ == '__main__':
    users_list = b'[{"email":"tw", "password":"xxx"}, {"email":"abc", "password":"xxx"}]'
    users_list_str = users_list.decode("utf-8")
    json = json.loads(users_list_str)
    flag = False
    for user in json:
        print(user)
        if user['email'] is 'tw':
            flag = True

    print(flag)
