
class Foo(object):
    def __init__(self, value=42):
        self.somevar = value

    def hello(self):
        print('sad')


f = Foo(1)
print("f.somevar=%d" % f.somevar)
f.hello()


class B(Foo):
    def __init__(self, value=42):
        super().__init__(value)
        print("b init")

    def hello(self):
        print('helo')


# __len__(self)
'''
so sad
 '''


def check_index(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class Arich:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        print("getitem")
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key*self.step

    def __setitem__(self, key, value):
        print("setitem")
        check_index(key)
        self.changed[key] = value


a = Arich(1, 2)
a[5] = 3
print(a[5])
# a.newvalue='qqq'
# print(a.newvalue)
# a.__getitem__(step)

b = B()
print(b.somevar)
b.hello()


class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.count = 0

    def __getitem__(self, index):
        self.count += 1
        return super(CounterList, self).__getitem__(index)


cc = CounterList(range(0, 200, 2))
# for item in range(0,100):
# cc.append(item)

# for i in range(0,100,2):
cc.reverse()
del cc[3:100]
print(cc)

print("!!!!!", cc.count)


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height
				
    size =property(get_size,set_size)

r = Rectangle()
r.width =10
r.height =3
print(r.size)
r.size=(1,2)
print(r.size)

class MyClass:
	@staticmethod
	def smeth():
		print("it's a static method")
	@classmethod
	def cmeth(cls):
		print('this is a class method of',cls)

MyClass.cmeth()
MyClass.smeth()2

