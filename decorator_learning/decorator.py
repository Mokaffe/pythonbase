"""
    decorator的原理: 装饰器本身就是一个函数，这个函数的参数是函数function
    装饰器的限制：
        1. 装饰函数要在被装饰函数前被定义
        2. 装饰函数包括两层：
            第一层：接收一个函数function
            第二层：构造一个函数来接收function的参数，然后在内部完成需要添加的功能并争取调用函数。
            然后在第一层返回第二层构造的这个函数。


"""


def log(func):
    def wrapper(*args, **kwargs):
        print("@log for %s" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


def decorator(func):
    def wrapper(*args):
        print("装饰器内部@decorator for %s" % func.__name__)
        func(*args)

    return wrapper


def hello(name):
    print("方法 本身 hello, %s" % name)


@decorator
def sugar_with_decorator(name):
    print("decorator with sugar, %s is new name" % name)


if __name__ == "__main__":
    print("\n-----0-------\n")
    new_hello_with_decorator = decorator(hello)
    new_hello_with_decorator("decorator")
    print(new_hello_with_decorator.__name__)

    print("\n-----1-------\n")
    print(hello.__name__)

    print("\n----2--------\n")
    sugar_with_decorator("doudou")
    print(sugar_with_decorator.__name__)
