import matplotlib.pyplot as plt

#折线图
x = [1,2,3,4,5,6,7,8]#点的横坐标
k1 = [1,1.92,1.62,2.39,2.41,3.14,3.26,3.90]#线1的纵坐标
k2 = [1,1.65,2.14,2.56,2.92,3.31,3.61,3.98]#线2的纵坐标
plt.plot(x,k1,'s-',color = 'r',label="speedup for view1")#s-:方形
plt.plot(x,k2,'o-',color = 'g',label="speedup for view2")#o-:圆形
plt.xlabel("thread nums")#横坐标名字
plt.ylabel("time accelerate")#纵坐标名字
plt.legend(loc = "best")#图例
plt.show()