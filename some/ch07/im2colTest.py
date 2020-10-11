import sys
import os
import sys
sys.path.append(os.pardir)
import numpy as np
from common.util import im2col
x1 = np.random.rand(1, 3, 7, 7)
col1 = im2col(x1, 5, 5, stride=1, pad=0)
# print(col1) # (9, 75)
x2 = np.random.rand(10, 3, 7, 7)  # 10 个数据
col2 = im2col(x2, 5, 5, stride=1, pad=0)
# print(col2) # (90, 75)


x = np.random.rand(1, 3, 4, 4)
w = np.random.rand(1, 3, 3, 3)
# b=np.array([1,1,2])

# print('x=', x)
# print('w=', w)

# class Convolution:
#   def __init__(self, W, b, stride=1, pad=0):
#     self.W = W
#     self.b = b
#     self.stride = stride
#     self.pad = pad
#   def forward(self, x):
#     FN, C, FH, FW = self.W.shape
#     N, C, H,W = x.shape
#     out_h = int(1 + (H + 2*self.pad - FH) / self.stride)
#     out_w = int(1 + (W + 2*self.pad - FW) / self.stride)
#     col = im2col(x, FH, FW, self.stride, self.pad)
#     col_W = self.W.reshape(FN, -1).T # 滤波器的展开
#     out = np.dot(col, col_W) + self.b
#     out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)
#     return out

# i=Convolution(w,)

arr=np.array([
    [2],
    [4],
    [3],
    [4],
    [4],
    [6],
    [3],
    [3],
    [4],
    [4],
    [4],
    [6],
])

print(arr.shape)
arr=arr.reshape(1,2,2,3)
print(arr)
arr=arr.transpose(0,3,1,2)
print(arr)
