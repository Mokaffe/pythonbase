def main(argv):
    if (argv
            or argv == 'test'):
        print('world')
    else:
        print(argv)


print("hello")

if __name__ == '__main__':
    main('aaa')
