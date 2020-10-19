import torch
import numpy as np

N, D_in, H, D_out = 64, 1000, 100, 10
"""
N,          D_in    ,H  ,D_out
训练个数　　　输入数量   隐藏层数量        输出数量
"""
x = torch.randn(N, D_in)  # 64*1000
y = torch.randn(N, D_out)  # 64*10
w1 = torch.randn(D_in, H, requires_grad=True)  #
w2 = torch.randn(H, D_out, requires_grad=True)
learning_rate = 1e-6
for t in range(500):
    # forward
    y_pred = x.mm(w1).clamp(min=0).mm(w2)
    # compute loss
    loss = (y_pred - y).pow(2).sum()
    print(t,loss.item())
    # backward pass
    # compute the gradient
    loss.backward()
    # update weights of w1 w2
    with torch.no_grad():
        w1 -= learning_rate * w1.grad
        w2 -= learning_rate * w2.grad
        w1.grad.zero_()
        w2.grad.zero_()
# print(y_pred-y)
