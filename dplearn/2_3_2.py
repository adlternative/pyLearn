import numpy as np
import matplotlib.pyplot as plt

# x = np.array([0, 1])
# w = np.array([0.5, 0.5])
# b = -0.7
# print(w*x)
# print(np.sum(w*x))
# print(np.sum(w*x)+b)

# 与门
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

# 与非门
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

# 或门
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1
#异或
def XOR(x1,x2):
  s1=NAND(x1,x2)
  s2=OR(x1,x2)
  y=AND(s1,s2)
  return y

s=XOR(0,0)
print(s)
