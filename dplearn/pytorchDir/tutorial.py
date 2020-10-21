import torch
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
from torch.autograd import Variable


def func():
    x = torch.linspace(-5, 5, 200)
    x = Variable(x)
    x_np = x.data.numpy()
    y_relu = torch.relu(x).data.numpy()
    y_sigmoid = torch.sigmoid(x).data.numpy()
    y_tanh = torch.tanh(x).data.numpy()
    y_soft = F.softplus(x).data.numpy()

    plt.figure(1, figsize=(8, 6))
    plt.subplot(221)
    plt.plot(x_np, y_relu, c='red', label='relu')
    plt.ylim((-1, 5))
    plt.legend(loc='best')
    plt.show()


x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
# x^2+0.2*0.2*(100)
y = x.pow(2) + 0.2 * torch.rand(x.size())
x, y = Variable(x), Variable(y)

plt.scatter(x.data.numpy(), y.data.numpy())
plt.show()


class Net(torch.nn.Module):
    def __init__(self, n_features, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_features, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_output)

    def forword(self, x):
        # 通过hidden+relu
        x = torch.relu(self.hidden(x))
        # 通过将隐藏层－>输出层
        x = self.predict(x)
        return x
net = Net(1,10,1)
print(net)
optimizer =torch.optim.SGD(net.parameters(),lr=0.5)
loss_func = torch.nn.MSELoss()
for t in range(100):
    prediction =net(x)
    loss = loss_func(prediction,y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()