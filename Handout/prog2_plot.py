import matplotlib.pyplot as plt

#折线图
x = [2,4,8,16]#点的横坐标
k1 = [82.9,76.7,73.4,72]#线1的纵坐标
# k2 = [1,1.65,2.14,2.56,2.92,3.31,3.61,3.98]#线2的纵坐标
plt.plot(x,k1,'s-',color = 'r',label="vector util")#s-:方形
# plt.plot(x,k2,'o-',color = 'g',label="speedup for view2")#o-:圆形
plt.xlabel("VECTOR_WIDTH")#横坐标名字
plt.ylabel("vector utilization(%)")#纵坐标名字
plt.legend(loc = "best")#图例
plt.show()