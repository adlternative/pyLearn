def func(*args):
	print(type(args))
	print(args)
	for item in args:
		print(item)
def fun2(**kargs):
	print(type(kargs),'\n',kargs)
	for item in kargs.keys():
		print(item,kargs[item])
	return kargs
func((1,2,3))
func()
func(*(1,2,3))
s=fun2(id=1,name=2,city='sad')
print(s)