import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
h = 0.001 # 求解步长

# 求解区间
a = 0
b = 200

# 在求解区间内间隔 h 取点作为 x 数组
t = np.arange(a, b+h, h)
# 定义和 x 形状相同的数组存贮数值解的值
x = np.zeros(t.shape)
y = np.zeros(t.shape)
# 计算解析解

x[0]=0 # 设置初始值
y[0]=1
# 开始计算
for i in range( len(t) - 1 ):
    x[i+1]=x[i]+(0.1*x[i]-0.01*x[i]*y[i])*h
    y[i+1]=y[i]+(-0.05*y[i]+0.2*x[i]*y[i])*h
    
    






fig = plt.figure(dpi = 144)
ax = fig.gca()
ax.plot(x, y, 'k-', label="数值解")
ax.legend(loc="upper left")



fig.savefig('picture3步长0.001,0-200,起始点(0,1).png',dpi=720)
# plt.savefig("./1.jpg")
plt.show()