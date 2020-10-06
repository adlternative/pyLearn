import numpy as np
import matplotlib.pylab as plt
if __name__ == '__main__':
  A=np.array([1,2,3,4])
  # A=np.array([1,2,3,4])
  print(np.ndim(A))
  print(A.shape)
  print(A.shape[0])
  B=np.array([[1,2],[3,4],[5,6]])
  print(B)
  print(np.ndim(B))
  print(B.shape)