'''

nested =[[1,2],[3,4],[5]]
def flatten(nested):
	for sublist in nested :
		for element in sublist:
			yield element

print(list(flatten(nested)))
g= (i**2 for i in range(2,23) )
print(type(g),next(g),sum(g),end='',sep='_')
 '''
''' try:
	[1,2]+'ads'
except TypeError as e:
	print(e)
	# pass
	  '''

'''
def flatten(nested):
	try:
		if isinstance(nested, str)==True:
				raise TypeError
		else:
				pass
		for sublist in nested:
			for element in flatten(sublist):
				yield element
	except TypeError:
		yield nested


nested =[[1,[2,"asd",[4]]],[1,4],[5]]

print(list(flatten(nested)))


def simple_generator():
	yield 1
print (simple_generator)
print (simple_generator())
print (list(simple_generator()))
def repeater(value):
	while True:
		new =(yield value)
		if new is not None :value =new
		else:
			print("??")
r =repeater(42)
print(next(r))
r.send('２')
print(next(r))
r.send('１')
print(next(r))
r.send('３')
print(next(r))
print(next(r))
print(next(r))
print(next(r))
 '''

''' def test():
	i=0
	while i < 5:
		temp =yield i
		print(temp)
		i +=1

a= test()
print(next(a))
# a.send('sad')
print(next(a))
print(next(a))
print(next(a))
 '''


def test(val=0):
		while True:
			y = yield val
			print(y, type(y))
			if(y is not None):
				val = y
			else:
				val = None

t = test()
print(t.send(None))
print(next(t))
print(t.send('asd'))
print(t.send(1123))
print(next(t))
print(next(t))
