# #coding:utf-8
# import numpy as np
# # 坐标向量
# a = np.array([1,2,3])
# # 坐标向量
# b = np.array([7,8])
# # 从坐标向量中返回坐标矩阵
# # 返回list,有两个元素,第一个元素是X轴的取值,第二个元素是Y轴的取值
# res = np.meshgrid(a,b)
# #返回结果: [array([ [1,2,3] [1,2,3] ]), array([ [7,7,7] [8,8,8] ])]
# print(res)

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([[0, 1, 2], [0, 1, 2]])
# y = np.array([[0, 0, 0], [1, 1, 1]])


# plt.plot(x, y,
#          color='r',  		# 全部点设置为红色
#          marker='.',  	# 点的形状为圆点
#          linestyle='-.')  # 线型为-.，也即点与点之间不用线连接
# plt.grid()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2])
y = np.array([0, 1])

X, Y = np.meshgrid(x, y)
print(X)
print(Y)


plt.plot(X, Y,
         color='red',  	# 全部点设置为红色
         marker='.',  	# 点的形状为圆点
         linestyle='')  # 线型为空，也即点与点之间不用线连接
plt.grid(True)
plt.show()
