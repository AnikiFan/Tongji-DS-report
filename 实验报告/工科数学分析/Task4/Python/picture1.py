import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
# 定义导函数
def dy(y):
    return y*(1/5-y/25) 
    
h = 0.001 # 求解步长

# 求解区间
a = 0
b = 20

# 在求解区间内间隔 h 取点作为 x 数组
x = np.arange(a, b+h, h)
# 定义和 x 形状相同的数组存贮数值解的值
w = np.zeros(x.shape)
# 计算解析解
y = 5-(20/(np.exp(x/5)+4))
w[0] = 1 # 设置初始值
# 开始计算
for i in range( len(x) - 1 ):
    w[i+1] = w[i] + h * dy(w[i])
    
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y, 'r-', label="解析解")
ax.plot(x, w, 'g--', label="数值解,步长为0.001")

X, Y = np.meshgrid(np.arange(0, 20, 1), np.arange(0, 10, .5))
U = 1
V = Y*(0.2-0.04*Y)
Q = ax.quiver(X, Y, U, V, units='width')
qk = ax.quiverkey(Q, 0.9, 0.9, 1, r'$1$单位', labelpos='E',
                   coordinates='figure')

ax.legend(loc="upper left")

fig.savefig('picture1.png',dpi=720)  


plt.ylim(ymin=0,ymax=10)
plt.show()