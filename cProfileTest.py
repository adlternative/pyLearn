import cProfile

def fibonaqi(n):
	if n==1:
		return 1
	if n==2:
		return 1
	return fibonaqi(n-1)+fibonaqi(n-2)

cProfile.run('fibonaqi(30)')
