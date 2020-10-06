import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    # y = x > 0
    # return y.astype(np.int)
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    return 1/(1+np.exp(-x))
  # 1/1+e^-100=1 1/1+e^0=0.5 1/1+e^-100=0

if __name__ == '__main__':
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()
