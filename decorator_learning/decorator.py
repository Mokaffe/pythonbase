def log(func):
    def wrapper(*args, **kwargs):
        print("call %s" % func.__name__)
        return func(*args, **kwargs)

    return wrapper
