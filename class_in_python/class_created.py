"""
    因为私有属性是不能够在类外通过实例对象来进行访问的。

    私有属性可以通过在get set 方法上设置 @property 来解决调用属性问题

    在Python中没有像C++中public和private这些关键字来区别公有属性和私有属性，
    它是以属性命名方式来区分，
    如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，否则为公有属性
    （方法也是一样，方法名前面加了2个下划线的话表示该方法是私有的，否则为公有的）
"""


class People:

    @property
    def name(self):
        return self.__name

    def age(self):
        return self.__age

    # __init__(self, ...) 是构造方法， 构造方法支持重载，
    # 构造方法支持重载，如果用户自己没有重新定义构造方法，系统就自动执行默认的构造方法。
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 析构方法 __del__(self) 在释放对象时调用，支持重载。
    # 可以在里面进行一些释放资源的操作，不要显示调用
    def __del__(self):
        print("析构方法")


people = People('hbao', 12)
print(people.age())
print(people.name)
