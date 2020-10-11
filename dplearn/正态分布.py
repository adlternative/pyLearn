#-*- coding:utf-8 -*-
# Python实现正态分布
# 绘制正态分布概率密度函数
import numpy as np
import matplotlib.pyplot as plt
import math
μ = 0  # 均值μ

# u01 = -2
δ = math.sqrt(0.2) # 标准差δ
x = np.linspace(μ - 3*δ, μ + 3*δ, 50)
y_δ = np.exp(-(x - μ) ** 2 /(2* δ **2))/(math.sqrt(2*math.pi)*δ)
print (x)
print ("="*20)
print( y_δ)
plt.plot(x, y_δ, "r-", linewidth=2)
plt.grid(True)
plt.show()