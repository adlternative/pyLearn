import torch
import numpy as np

N, D_in, H, D_out = 64, 1000, 100, 10
"""
N,          D_in    ,H  ,D_out
训练个数　　　输入数量   隐藏层数量        输出数量
"""
x = torch.randn(N, D_in)  # 64*1000
y = torch.randn(N, D_out)  # 64*10
w1 = torch.randn(D_in, H)  #
w2 = torch.randn(H, D_out)
learning_rate = 1e-6
for t in range(500):
    #forward
    h = x.mm(w1)
    h_relu = h.clamp(min=0)
    y_pred = h_relu.mm(w2)
    #compute loss
    loss =(y_pred-y).pow(2).sum().item()
    # print(type(loss))
    print(t,loss)
    #backward pass
    #compute the gradient
    grad_y_pred =2.0*(y_pred-y)
    grad_w2=h_relu.t().mm(grad_y_pred)
    grad_h_relu= grad_y_pred.mm(w2.t())
    grad_h=grad_h_relu.clone()
    grad_h[h<0]=0
    grad_w1=x.t().mm(grad_h)
    w1-=learning_rate*grad_w1
    w2-=learning_rate*grad_w2
    #update weights of w1 w2
# print(y_pred-y)
