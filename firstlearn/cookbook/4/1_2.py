def fun1():
    """
        next + try except stopIter
    """
    with open('/etc/passwd')as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass


def fun2():
    """next + None """
    with open('/etc/passwd')as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')


def fun3():
    """iter +next"""
    items = [1, 2, 3]
    it = iter(items)
    print(next(it))
    print(next(it))
    print(next(it))
    # print(next(it))


if __name__ == '__main__':
    fun3()
