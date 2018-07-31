"""
    https://blog.theerrorlog.com/simple-lru-cache-in-python-3.html
"""


class T:
    @property
    def aa(self):
        print("property as dict")


class Foo:
    @property
    def name(self):
        print("name")

    # @property
    # def as_dict(self):
    #     print("dict")

    def as_dict(self):
        print("sss" + self.__name)

    def __init__(self, name):
        self.__name = name


if __name__ == "__main__":
    foo = Foo('Lily')
    t = T()
    print(hasattr(t.as_dict, "__call__"))
