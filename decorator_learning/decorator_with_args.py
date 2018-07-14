def decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("装饰器本身的参数 %s and %s" % (arg1, arg2))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@decorator_with_args("hello", "doudou")
def func_with_args(name):
    print("decorator with args 函数也有参数 %s" % name)


if __name__ == "__main__":
    func_with_args("func的参数")
