"""
    将整个类作为一个装饰器，工作流：
    (1) 通过 __int__() 方法初始化类
    (2) 通过 __call__() 方法调用真正的装饰方法

    当装饰器有参数的时候，init() 成员就不能传入 func 了？而 func 是在call() 的时候传入。
    （func 代表要装饰的函数）
"""
from functools import wraps
from inspect import getcallargs


class MakeHtmlTag(object):

    def __init__(self, tag, css_class=""):
        self._tag = tag
        self._css_class = " class='{0}'".format(css_class) if css_class != "" else ""

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return "<" + self._tag + self._css_class + ">" + func(*args, **kwargs) + "</" + self._tag + ">"

        return wrapper


@MakeHtmlTag("b", css_class="bold_css")
@MakeHtmlTag("i", css_class="italic_css")
def hello(name):
    return "hello, {}".format(name)


# print(hello("hbao"))


class Logger(object):
    def __init__(self, filename=''):
        if filename != '':
            self._filename = filename
        else:
            self._filename = 'log/error_log'

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_args = getcallargs(func, *args, **kwargs)
            if 'param1' in func_args.keys():
                param1 = func_args['param1']
            if 'param2' in func_args.keys():
                param2 = func_args['param2']

            with open(self._filename, 'a') as logfile_handle:
                logfile_handle.write(param1 + '/' + param2 + '\t finished\n')
                logfile_handle.flush()

            return func(*args, **kwargs)

        return wrapper


@Logger(filename='test_log')
def test(param1, param2, param3, param4, param5):
    print('ok, finished')
    return param5


if __name__ == '__main__':
    print(test('1', '2', '3', '4', '5'))
    print(test('s', 'g', 'r', 'e', 'b'))
