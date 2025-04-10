import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

h=0.1
# plt.savefig("./1.jpg")

# 在求解区间内间隔 h 取点作为 x 数组
t = np.linspace(0,1,10)
# 定义和 x 形状相同的数组存贮数值解的值
X = np.zeros(t.shape)
Y = np.zeros(t.shape)
Z = np.zeros(t.shape)
# 计算解析解

X[0]=-1 # 设置初始值
Y[0]=1
Z[0]=-1
# 开始计算
for i in range( len(t) - 1 ):
    X[i+1]=X[i]+10*(Y[i]-X[i])*h
    Y[i+1]=Y[i]+(28*X[i]-Y[i]-X[i]*Z[i])*h
    Z[i+1]=Z[i]+(X[i]*Y[i]-8*Z[i]/3)*h
 
fig= plt.figure()    
ax= fig.add_subplot(projection='3d')  
ax.plot(X,Y,Z,'k-', label="数值解,t:0-1,步长为0.1")  
ax.legend(loc="upper left")

fig.savefig('picture4步长0.1,0-0.5,起始点(-1,1,-1).png',dpi=720)      
plt.show()
