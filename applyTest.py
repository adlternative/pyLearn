

import sys

help('apply')
sys.exit(0)
def function(a, b):
    print(a, b)


apply(function, ('good', 'better'))
apply(function, (2, 3+6))
apply(function, ('cai', 'quan'))
apply(function, ('cai',), {'b': 'caiquan'})
apply(function, (), {'a': 'caiquan', 'b': 'Tom'})
# --使用 apply 函数调用基类的构造函数


class Rectangle:
    def __init__(self, color="white", width=10, height=10):
        print ("create a", color, self, "sized", width, "x", height)


class RoundedRectangle(Rectangle):
    def __init__(self, **kw):
        apply(Rectangle.__init__, (self,), kw)


rect = Rectangle(color="green", height=100, width=100)
rect = RoundedRectangle(color="blue", height=20)
