import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig= plt.figure()    
ax= fig.add_subplot(projection='3d')  
h = 0.0001
# 求解区间
# 在求解区间内间隔 h 取点作为 x 数组
t = np.linspace(0,10,100000)
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
ax.plot(x,y,z,'y-', label="数值解1,t:0-10,步长为0.0001")       

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
ax.plot(x,y,z,'g-', label="数值解2,t:0-10,步长为0.001")       

h=0.01
# plt.savefig("./1.jpg")

# 在求解区间内间隔 h 取点作为 x 数组
t = np.linspace(0,10,1000)
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
 
ax.plot(X,Y,Z,'r-', label="数值解3,t:0-10,步长为0.01")


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
 
ax.plot(X,Y,Z,'k-', label="数值解4,t:0-1,步长为0.1")
ax.legend(loc="upper left")
fig.savefig('picture4起始点(-1,1,-1).png',dpi=720)   
plt.show()
