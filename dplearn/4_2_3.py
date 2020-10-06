import numpy as np
import sys
import os

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)


def cross_entropy_error(y, t):
    print(type(t))
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]

# s = mean_squared_error(np.array(y), np.array(t))
s = cross_entropy_error(np.array(y), np.array(t))
s2 = cross_entropy_error(np.array(y2), np.array(t))
print(s)
print(s2)
