"""
    并行迭代 zip:
        同时迭代多个序列，当序列长度不同时，函数zip将在最短的序列用完后停止"缝合"
"""

if __name__ == "__main__":
    names = ['Anna', 'Bob', 'Demo']
    ages = [12, 39, 29]
    hobbies = ['read', 'game', 'music']

    for i in range(len(names)):
        print(names[i], 'is', ages[i], 'years old')

    combine = zip(names, ages, hobbies)
    # [('Anna', 12), ('Bob', 39), ('Demo', 29)]
    # [('Anna', 12, 'read'), ('Bob', 39, 'game'), ('Demo', 29, 'music')]
    print(list(combine))
