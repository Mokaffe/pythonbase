import random
import string
# from werkzeug.security import generate_password_hash, check_password_hash


def generate_activation_code(length=16, n=10):
    '''生成n个长度为len的随机序列码'''
    random.seed()
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return [''.join([random.choice(chars) for _ in range(length)]) for _ in range(n)]


def generate_activation_password(length=16):
    random.seed()
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join([random.choice(chars) for _ in range(length)])


if __name__ == '__main__':
    print(generate_activation_password())
    # for index, code in enumerate(generate_activation_code(), 1):
    #     password_wrapper = generate_password_hash(code)
    #     print(index, code, password_wrapper)


