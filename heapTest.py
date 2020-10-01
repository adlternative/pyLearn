from heapq import *
from random import shuffle
data = list(range(10))
shuffle(data)
heap = []
for n  in data : 
	heappush(heap,n)
heappush(heap,11)
print(heap)
print("pop  :%d"%heappop(heap))
print("pop  :%d"%heappop(heap))
print("pop  :%d"%heappop(heap))
print("pop  :%d"%heappop(heap))
print("pop  :%d"%heappop(heap))

heap = [1,4,34,4,34,234,423]
heapify(heap)
heapreplace(heap,0.7)
print(heap)