from abc import ABC, abstractmethod
import sys
from warnings import warn,filterwarnings

class Sercetive:
    # print("sad")
    def __inaccessable(self):
        print("ha")

    def accessable(self):
        self.__inaccessable()
        print("he")


s = Sercetive()
s.accessable()
s._Sercetive__inaccessable()


def foo(x): return x*x


def foo(x): return x*x


print(foo(1))


class M:
    members = 0

    def init(self):
        M.members += 1


m1 = M()
m1.init()
print(m1.members)
m2 = M()
m2.init()
print(m1.members)
print(m2.members)
m1.members = ['sda', 'da']


class F:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SF(F):
    def init(self):
        self.blocked = ['S']


f = F()

f.init()
x = f.filter(['ss', 'sad', 'sda', 'ad', 'S', 'd'])
print(x)
ff = SF()
ff.init()
x = ff.filter(['ss', 'sad', 'sda', 'ad', 'S', 'd'])
print(x)
print(issubclass(SF, F), F.__bases__, SF.__bases__,
      isinstance(ff, SF), ff.__class__)


class C:
    a = 1

    def c(self, exp):
        self.value = eval(exp)


class T:
    def t(self):
        print('helo wold')


class TC(T, C):
    pass


tc = TC()
tc.c('1+2*3')
print(tc.value, hasattr(tc, 'c'), callable(getattr(tc, 'a', None)))
tc.t()
setattr(tc, 'a', -1)
print(tc.a)
print(tc.__dict__)


class Coll(ABC):
    @abstractmethod
    def talk(self):
        pass

# c= Coll()


class CollS(Coll):
    def talk(self):
        pass


c = CollS()
c.talk()


class Colns:
    def talk(self):
        pass


c = Colns()
print(isinstance(c, Coll))
print(issubclass(Colns, Coll))
Coll.register(Colns)
print(isinstance(c, Coll))
print(issubclass(Colns, Coll))
filterwarnings("ignore")
warn("??")
warn("??")
filterwarnings("error")
print("!")
try:
    warn("??")
except:
    filterwarnings("ignore",category=DeprecationWarning)
warn("this is a ",DeprecationWarning)
warn("this is a ")

# x = int(input('first'))
# y = int(input('first'))
# try:
#     print(x/y)

#     raise ArithmeticError
#     raise Exception
# except Exception:
#     print("ASd")
while(True):
    try:
        x = int(input('first'))
        y = int(input('first'))
        v=x/y
        print(v)
    except:
        print("invaild inout ,tru agiain")
        continue
    else:
        break
    finally:
        print("heheheh")
         
try:
    1/0
except (ZeroDivisionError, DeprecationWarning)as z:
    print("wowoowowoow\n\n\n", z)
    try:
        pass
        # while(True):
            # pass
        # "das"/sad
        # raise ValueError from None
    except:
        print("wowoowowoow\n\n\n")
        sys.exit(1)
    else:
        print("llala\n")


