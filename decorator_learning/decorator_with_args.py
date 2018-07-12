def decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("decorator with args %s and %s" % (arg1, arg2))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@decorator_with_args("hello", "doudou")
def func_with_args():
    print("decorator with args")


if __name__ == "__main__":
    func_with_args()
