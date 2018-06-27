import logging


def bar():
    pass


# def use_logging(func):
#     print('oooo %s', func.__name__)
#     logging.info("%s is running" % func.__name__)
#     func()


# use_logging(foo)


def use_logging_dec(func):
    def wrapper():
        print("%s is running" % func.__name__)
        return func

    return wrapper


@use_logging_dec
def foo():
    pass


if __name__ == "__main__":
    foo()
