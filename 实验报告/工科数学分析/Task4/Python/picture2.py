import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
# 定义导函数
def dy(y):
    return a+i*h+y+y*y
    
h = 0.001 # 求解步长

# 求解区间
a = 0
b = 2

# 在求解区间内间隔 h 取点作为 x 数组
x = np.arange(a, b+h, h)
# 定义和 x 形状相同的数组存贮数值解的值
w = np.zeros(x.shape)
# 计算解析解

w[0] = 1 # 设置初始值
# 开始计算
for i in range( len(x) - 1 ):
    w[i+1] = w[i] + h * dy(w[i])
    
fig = plt.figure(dpi = 144)
ax = fig.gca()
ax.plot(x, w, 'g--', label="数值解,步长为0.001")
ax.legend(loc="upper left")
# plt.savefig("./1.jpg")
h = -0.1 # 求解步长

# 求解区间
a = 0
b = -2

# 在求解区间内间隔 h 取点作为 x 数组
x = np.arange(a, b+h, h)
# 定义和 x 形状相同的数组存贮数值解的值
w = np.zeros(x.shape)
# 计算解析解

w[0] = 1 # 设置初始值
# 开始计算
for i in range( len(x) - 1 ):
    w[i+1] = w[i] + h * dy(w[i])
ax.plot(x, w, 'g--', label="数值解,步长为0.001")


X, Y = np.meshgrid(np.arange(-2, 2, .2), np.arange(-2, 2, .2))
U = 1
V = X+Y+Y*Y

Q = ax.quiver(X, Y, U, V, units='width')
qk = ax.quiverkey(Q, 0.9, 0.9, 3, r'$3$单位', labelpos='E',
                   coordinates='figure')

plt.ylim(ymin=-2,ymax=2)
fig.savefig('picture2步长0.001.png',dpi=720)
plt.show()