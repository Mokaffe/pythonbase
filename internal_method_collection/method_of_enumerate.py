"""
    内置函数 enumerate：
        当需要迭代并获取list的索引时，可以用enumerate
"""

if __name__ == "__main__":
    strings = ['abc', 'abd', 'efg', 'aad', 'sda']
    for index, string in enumerate(strings):
        if 'a' in string:
            strings[index] = '[censored]'

    print(strings)
