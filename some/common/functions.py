# coding: utf-8
import numpy as np


def identity_function(x):
    return x


def step_function(x):
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))    


def sigmoid_grad(x):
    return (1.0 - sigmoid(x)) * sigmoid(x)
    

def relu(x):
    return np.maximum(0, x)


def relu_grad(x):
    grad = np.zeros(x)
    grad[x>=0] = 1
    return grad

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T

    x = x - np.max(x) # 溢出对策
    return np.exp(x) / np.sum(np.exp(x))
if __name__ == '__main__':
    s=softmax(np.array([[1,2],[3,4]]))
    print(s)
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)


def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # 监督数据是one-hot-vector的情况下，转换为正确解标签的索引
    if t.size == y.size:
        t = t.argmax(axis=1)#横轴上正解的坐标

    batch_size = y.shape[0]
                              #0轴 1~100        ［1,2,3,4,4,5］１００个分别代表正解
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
# if __name__ == '__main__':
    # cross_entropy_error()
def softmax_loss(X, t):
    y = softmax(X)
    return cross_entropy_error(y, t)
