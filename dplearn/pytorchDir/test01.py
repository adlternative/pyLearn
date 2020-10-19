import torch
import numpy as np

N, D_in, H, D_out = 64, 1000, 100, 10
"""
N,          D_in    ,H  ,D_out
训练个数　　　输入数量   隐藏层数量        输出数量
"""
x = np.random.randn(N, D_in)  # 64*1000
y = np.random.randn(N, D_out)  # 64*10
w1 = np.random.randn(D_in, H)  #
w2 = np.random.randn(H, D_out)
learning_rate = 1e-6
for t in range(500):
    #forward
    h = x.dot(w1)
    h_relu = np.maximum(h, 0)
    y_pred = h_relu.dot(w2)
    #compute loss
    loss =np.square(y_pred-y).sum()
    print(t,loss)
    #backward pass
    #compute the gradient
    grad_y_pred =2.0*(y_pred-y)
    grad_w2=h_relu.T.dot(grad_y_pred)
    grad_h_relu= grad_y_pred.dot(w2.T)
    grad_h=grad_h_relu.copy()
    grad_h[h<0]=0
    grad_w1=x.T.dot(grad_h)
    w1-=learning_rate*grad_w1
    w2-=learning_rate*grad_w2
    #update weights of w1 w2
# print(y_pred-y)
