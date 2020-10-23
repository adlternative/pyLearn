from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


def func():
    try:
        with open('somefile.txt') as f:
            lines = linehistory(f)
            for line in lines:
                print('{}'.format(line), end='')
            print()
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')
    except FileNotFoundError:
        pass
def func2():
    f=open('somefile.txt')
    lines=linehistory(f)
    next(lines)

func2()
