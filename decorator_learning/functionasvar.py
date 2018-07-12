"""
    函数也是对象，函数对象可以被赋值给变量，所以，通过变量也能调用函数
"""
from decorator_learning.decorator import log

"""
    函数作为一个对象，拥有对象模型的通用属性：id,类型和值
    使用id加函数名，可以打印func这个函数在内存中的身份地址;
    使用type加函数名可以打印func这个函数的类型;
    只输入函数名，不加括号时，会输出函数在内存中的地址;
    只有输入函数名加括号时，函数才会被调用。
"""


@log
def bar():
    print(type)
    print("2018年07月06日13:44:38")
    print(id(bar))
    print(type(bar))
    print(bar)


if __name__ == "__main__":
    # TODO: 为什么不是 f = bar()
    f = bar
    # TODO: 为什么是写f(), 当我只写f，不加（）时，没有任何输出
    f()
    print("\n----------ss------\n")
    print(id(f))

"""
    现在我们要增强bar()函数的功能--在bar()函数调用的前后自动打印日志，
    但是又不希望修改bar()函数的定义，这种在代码运行期间动态增加功能的方式，
    称之为"装饰器 Decorator"
"""
