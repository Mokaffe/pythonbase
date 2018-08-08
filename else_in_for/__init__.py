"""
    书本里介绍的是： 循环中的else子句
"""
from math import sqrt

if __name__ == "__main__":
    a = range(50, 89)
    for n in a:
        print(n)
        root = sqrt(n)
        print(root)
        if root == int(root):
            print(n)
            break

    else:
        print("Did't fin it!")
