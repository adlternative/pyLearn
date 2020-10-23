class A(object):
    size = "sad"

    def __init__(self):
        self.color = 'white'
        print("super:A")

    def output(self):
        print(self.size)


class Dog(A):
    def __init__(self):
        self.name = 'dog'
        print('subClass:d')

    def run(self):
        print(Dog.size, self.color, self.name)
        A.output(self)


class Cat(A):
    def __init__(self):
        # A.__init__(self)
        self.name = 'cat'
        print("subClass:c")

    def run(self):
        print(Cat.size, self.color, self.name)
        super(Cat, self).__init__()
        super().output()


a = A()
a.output()
dog = Dog()
dog.size='mid'
dog.color='black'
dog.run()
cat =Cat()
cat.name= 'maomi'
cat.run()
