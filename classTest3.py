class Rect:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        if(name == 'size'):
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if(name == 'size'):
            return self.width, self.height
        else:
            raise AttributeError()


rect = Rect()
rect.size = (1, 2)
print(rect.size)
rect.si = 1


class Fibs(object):
    def __init__(self):
        self.a = 1
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        return self.a

    def __iter__(self):
        return self


f = Fibs()
iter = iter(f)
for i in f:
    if i > 40:
        print(i)
        break
# it =iter([1,2,3])
print(next(f))

class TestInterator:
	value =0
	def __next__(self):
		self.value +=1
		if self.value>10:raise StopIteration
		return self.value
	def __iter__(self):
		return self
	
ti =TestInterator()
print(list(ti))