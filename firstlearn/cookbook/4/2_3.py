class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


# Example
def func1():
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)


# Outputs Node(1), Node(2)
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')


if __name__ == '__main__':
    s = countdown(4)
    while True:
        try:
            print(next(s))
        except StopIteration as e:
            break

