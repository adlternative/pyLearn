class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


def func():
    a=reversed(Countdown(4))
    while True:
        s=next(a,None)
        if not s :
            break
        print(s)
if __name__ == '__main__':
    func()
