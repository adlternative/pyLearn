import pprint

import torch
import numpy as np


def dif_of_numpy_and_torch():
    x_numpy = np.array([0.1, .2, .3])
    x_torch = torch.tensor([.1, .2, .3])
    print(x_numpy, x_torch, sep='\n')
    print(torch.from_numpy(x_numpy), x_torch.numpy(), sep='\n')
    y_numpy = np.array([3, 4, 5])
    y_torch = torch.tensor([3, 4, 5])
    print(x_numpy + y_numpy, x_torch + y_torch)
    # 根号 0.1^2+0.2^2+0.3^2
    print(np.linalg.norm(x_numpy), torch.norm(x_torch))
    x_numpy = np.array([[1, 2], [3, 4]])
    x_torch = torch.FloatTensor([[1, 2], [3, 4]])
    # 平均 axis指的是（1+3）/2 = 2 （2+4）/2 =3，列为0,行为1
    print(np.mean(x_numpy, axis=0))
    print(torch.mean(x_torch, dim=0))


def TensorView():
    N, C, W, H = 10000, 3, 28, 28
    X = torch.randn((N, C, W, H))
    print(X.shape)
    print(X.view(N, C, 784).shape)
    print(X.view(-1, C, 784).shape)


def broadcasting_in_tensor():
    x = torch.empty(5, 1, 4, 1)
    y = torch.empty(3, 1, 3)
    print((x + y).shape)


def cuda_sementics():
    # 无法使用
    cpu = torch.device('cpu')
    gpu = torch.device('cuda')
    x = torch.rand(10)
    h = torch.
    print(x)
    x = x.to(gpu)
    print(x)
    x = x.to(cpu)
    print(x)


def g(w):
    return 2 * w[0] * w[1] + w[1] * torch.cos(w[0])


def grad_g(w):
    return torch.tensor([2 * w[1] - w[1] * torch.sin(w[0]), 2 * w[0] + torch.cos(w[0])])


def gradTest():
    w = torch.tensor([np.pi, 1], requires_grad=True)
    print(w)
    z = g(w)
    z.backward()
    print('Anal grad g(w)', grad_g(w))
    print('PyTorch\'s grad g(w)', w.grad)


def gradTest2():
    x = torch.tensor([5.0], requires_grad=True)
    step_size = 0.25
    # for i in range(15):
    #     y = f(x)
    #     y.backward()
    #     print(i,x.item(),f(x).item(),fp(x).item(),fp(x).item,x.grad.item())
    #     x.data =x.data-step_size*x.grad
    #     x.grad.detach()
    #     x.grad.zero()

if __name__ == '__main__':
    gradTest()
    # dif_of_numpy_and_torch()
    # TensorView()
    # broadcasting_in_tensor()
    # cuda_sementics()

    pass
