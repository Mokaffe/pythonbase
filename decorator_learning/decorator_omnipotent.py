"""
    装饰器原理， 带有装饰器的函数已经变成了经过装饰器修饰的方法

    Python 的 functool 包中提供了一个叫 wrap 的 decorator 来消除这样的副作用
"""

import time
from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = time.time()
        print('satrt run the function %s' % func.__name__)
        result = func(*args, **kwargs)
        time_end = time.time()
        print('run end! it continue %.2f' % (time_end - time_start))
        return result

    return wrapper


@logger
def hello():
    print('start running')
    time.sleep(2)
    return 2


hello()
# 在没有加@wrap之前打印出来的 hello.__name__ 结果是 wrapper
# 用@wrap 去消除装饰器的影响时，打印的结果是 hello
print(hello.__name__)
