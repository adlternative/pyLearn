import numpy as np

b = np.arange(12).reshape(3,4)
print(b)

print(b.sum(axis=0))
print(b.shape)
print(b.sum(axis=1))
c=np.arange(3)
t=np.array([1,3,3])

print("c="%c)

print(b[c,t])