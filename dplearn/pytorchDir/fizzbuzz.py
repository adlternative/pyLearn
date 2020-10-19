import torch
import numpy as np

NUM_DIGIT = 10


def fizz_buzz_encode(i):
    if i % 15 == 0:
        return 3  # fizzbuzz
    elif i % 5 == 0:
        return 2  # buzz
    if i % 3 == 0:
        return 1  # fizz
    else:
        return 0


def fizz_buzz_decode(i, prediction):
    return [str(i), "fizz", "buzz", "fizzbuzz"][prediction]


def helper(i):
    fizz_buzz_decode(i, fizz_buzz_encode(i))


def binary_encode(i, num_digits):
    """

    :param i:
    :param num_digits:
    :return: np.array([i >> d & 1 for d in range(num_digits)][::-1])
    binary_encode(10,10)==np.array([0,0,0,0,0,0,1,0,1,0])
    """
    return np.array([i >> d & 1 for d in range(num_digits)][::-1])


# 训练的输入,注意到是从101~1024
trX = torch.Tensor([binary_encode(i, NUM_DIGIT) for i in range(101, 2 ** NUM_DIGIT)])
# 训练的正确输出
trY = torch.LongTensor([fizz_buzz_encode(i) for i in range(101, 2 ** NUM_DIGIT)])
# print(trX)
# print(trY)

NUM_HIDDEN = 100
model = torch.nn.Sequential(
    torch.nn.Linear(NUM_DIGIT, NUM_HIDDEN),
    torch.nn.ReLU(),
    torch.nn.Linear(NUM_HIDDEN, 4),
)
loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.05)

BATCH_SIZE = 128
for epoch in range(10000):
    for start in range(0, len(trX), BATCH_SIZE):
        end = start + BATCH_SIZE
        batchX = trX[start:end]
        batchY = trY[start:end]
        y_pred = model(batchX)
        loss = loss_fn(y_pred, batchY)
        print("Epoch", epoch, loss.item())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

testX = torch.Tensor([binary_encode(i, NUM_DIGIT) for i in range(1, 101)])
with torch.no_grad():
    textY = model(testX)
    predictions = zip(range(1, 101), textY.max(1)[1].data.tolist())
    print([fizz_buzz_decode(i, x) for i, x in predictions])
