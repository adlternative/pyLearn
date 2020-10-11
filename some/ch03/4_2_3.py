import numpy as np
import sys
import os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist


(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=False)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

# print(x_batch.shape)  # 10,784
# print(t_batch.shape)  # 10,10 |10,

# def mean_squared_error(y, t):
#     return 0.5 * np.sum((y-t)**2)
t2= [1,2,3]

y2 = np.array([
    [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0],
    [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0],
    [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0],
])

# print(y2.shape)
# print(y2[np.arange(3),np.array([2,9,4])])
# s=-np.sum(np.log(arepl-backend/python/arepl_jsonpickle/ext/numpy.py:298: Usery2[np.arange(3),np.array([2,9,4])]+1e-7))/3
# print(s)
def cross_entropy_error(y, t):
    # print(type(t))
    delta = 1e-7
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + delta))/batch_size

def cross_entropy_error2(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
print(cross_entropy_error2(y2,t2))

# print(cross_entropy_error(x_batch,t_batch))
# t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
# y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]

# # s = mean_squared_error(np.array(y), np.array(t))
# s = cross_entropy_error(np.array(y), np.array(t))
# s2 = cross_entropy_error(np.array(y2), np.array(t))
# print(s)
# print(s2)
