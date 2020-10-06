import numpy as np
import matplotlib.pylab as plt
a = np.array([0.3, 2.9, 4.0])
# exp_a = np.exp(a)  # 指数函数
# print(exp_a)

# sum_exp_a = np.sum(exp_a)  # 指数函数的和
# print(sum_exp_a)

# y = exp_a / sum_exp_a
# print(y)


def softmax(a):
    '''
      return e^0.3/(e^0.3+e^2.9+e^4.0)
    '''
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


if __name__ == '__main__':
    print(softmax(a))
