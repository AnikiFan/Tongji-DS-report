import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

h = 0.001
# 求解区间
# 在求解区间内间隔 h 取点作为 x 数组
t = np.linspace(0,10,10000)
# 定义和 x 形状相同的数组存贮数值解的值
x = np.zeros(t.shape)
y = np.zeros(t.shape)
z = np.zeros(t.shape)
# 计算解析解x[0]=-1 # 设置初始值
x[0]=-1
y[0]=1
z[0]=-1
# 开始计算
for i in range( len(t) - 1 ):
    x[i+1]=x[i]+10*(y[i]-x[i])*h
    y[i+1]=y[i]+(28*x[i]-y[i]-x[i]*z[i])*h
    z[i+1]=z[i]+(x[i]*y[i]-8*z[i]/3)*h
fig= plt.figure()    
ax= fig.add_subplot(projection='3d')  
ax.plot(x,y,z,'g-', label="数值解,t:0-10,步长为0.001")    
ax.legend(loc="upper left")

fig.savefig('picture4步长0.001,0-10,起始点(-1,1,-1).png',dpi=720)      
plt.show()
