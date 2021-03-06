# coding: utf-8
# cf.http://d.hatena.ne.jp/white_wheels/20100327/p3
import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D


def _numerical_gradient_no_batch(f, x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)  # f(x+h)
        x[idx] = tmp_val - h
        fxh2 = f(x)  # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val  # 还原值

    return grad
# 返回梯度
def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)

        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)

        return grad


def function_2(x):
    if x.ndim == 1:
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1)
# print(function_2(np.array([[1,3],[2,4]])))
# s1,s2,s3=_numerical_gradient_no_batch(function_2, np.array([3.0, 4.0])),_numerical_gradient_no_batch(function_2, np.array([0.0, 2.0])),_numerical_gradient_no_batch(function_2, np.array([3.0, 0.0]))
# print(s1,s2,s3)
def tangent_line(f, x):
    d = numerical_gradient(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y
# 返回导数函数f'

if __name__ == '__main__':
    x0 = np.arange(-2, 2.5, 0.25)
    x1 = np.arange(-2, 2.5, 0.25)
    X, Y = np.meshgrid(x0, x1)#生成网格点坐标矩阵。
    print(X.shape)
    X = X.flatten()#将多维数组降为一维
    Y = Y.flatten()
    print(X)

    grad = numerical_gradient(function_2, np.array([X, Y]))

    plt.figure()#创建自定义图像

    # ,headwidth=10,scale=40,color="#444444")
    plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy", color="#666666")#箭头

    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.xlabel('x0')
    plt.ylabel('x1')

    plt.grid()#显示网格
    plt.legend()#给图加上图例,右上角小方块
    plt.draw()#可显示后修改i
    plt.show()#显示
