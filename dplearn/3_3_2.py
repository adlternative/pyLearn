import numpy as np
import matplotlib.pylab as plt
if __name__ == '__main__':
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = np.array([[1, 2, 3], [4, 5, 6]])
    D = np.array([[1, 2, 3, 4], [4, 2, 3, 5], [3, 4, 5, 4]])

    E = np.array([[1, 2], [3, 4], [4, 5]])
    F = np.array([5, 6])
    # print(E.shape)
    # print(F.shape)
    print(np.dot(E, F))

    X = np.array([1, 2])
    W = np.array([[1, 3, 5], [2, 4, 6]])
    print(X.shape)
    print(W.shape)
    print(np.dot(X, W))
