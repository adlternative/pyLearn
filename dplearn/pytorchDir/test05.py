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


class TwoLayerNet(torch.nn.Module):
    def __init__(self, D_in, H, D_out):
        super(TwoLayerNet, self).__init__()
        self.linear1 = torch.nn.Linear(D_in, H, bias=False)
        self.linear2 = torch.nn.Linear(H, D_out, bias=False)

    def forward(self, x):
        y_pred = self.linear2(self.linear1(x).clamp(min=0))
        return y_pred


model = TwoLayerNet(D_in, H, D_out)
# model = torch.nn.Sequential(
#     torch.nn.Linear(D_in, H, bias=False),
#     torch.nn.ReLU(),
#     torch.nn.Linear(H, D_out, bias=False),
# )
# torch.nn.init.normal_(model[0].weight)
# torch.nn.init.normal_(model[2].weight)
lose_fn = torch.nn.MSELoss(reduction='sum')
learning_rate = 1e-4
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
for t in range(500):
    # forward
    y_pred = model(x)
    # compute loss
    loss = lose_fn(y_pred, y)
    print(t, loss.item())
    # backward pass
    # compute the gradient
    optimizer.zero_grad()

    loss.backward()

    optimizer.step()
