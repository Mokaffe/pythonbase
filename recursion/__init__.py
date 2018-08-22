import os

if __name__ == "__main__":
    content = ['env = dev\n', 'auth = basic abcd==']
    config = {}

    for line in content:
        index = int(line.find('='))
        print(type(index + 1))
        config[line[0:index].strip()] = line[index + 1:].strip()

    print(config)
