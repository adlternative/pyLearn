import torch
import numpy as np

# print(np.dot.__doc__)
from torch.autograd import Variable

np_data = np.arange(6).reshape((2, 3))

# numpy转torch
torch_data = torch.from_numpy(np_data)
t2 = torch_data.numpy()
# torch转numpy
print(t2)
print(torch_data)

# list转tensor
data = [-1, -2, 1, 2]
tensor = torch.FloatTensor(data)
print(tensor)
print(
    # sin
    '\nnp.sin', np.sin(data),
    '\ntorch.sin', torch.sin(tensor),
    # 绝对值
    '\ntorch.abs', torch.abs(tensor),
    # 平均
    '\ntorch.mean', torch.mean(tensor),
    # 平均
    '\ntorch.mean', torch.mean(tensor),
)
data = [[1, 2], [3, 4]]
tensor = torch.FloatTensor(data)
data = np.array(data)
print(
    # 矩阵乘法
    '\n np.matmul', np.matmul(data, data),
    '\n torch.mm', torch.mm(tensor, tensor),
    # dot
    '\n np.matmul', data.dot(data),
    # '\n torch.mm', tensor.dot(tensor),
)

variable = Variable(tensor, requires_grad=True)

# '\n torch.mean', torch.mean(tensor*tensor),# [2,2]
# '\n torch.var', torch.mean(variable*variable),
t_out =torch.mean(tensor*tensor)
v_out = torch.mean(variable * variable)
v_out.backward()
print('',t_out,
    v_out,
    variable.grad,
    variable.data.numpy(),
sep='\n'
)
