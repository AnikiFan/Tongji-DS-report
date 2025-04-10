######################第一段代码演示开始
def dy(y):
    return F(a+i*h,y)
# 定义导函数    

h = step length # 求解步长

a = x_0
b = end value
# 求解区间端点值

x = np.arange(a, b+h, h)# 在求解区间内间隔 h 取点作为 x 数组

y = np.zeros(x.shape)# 定义和 x 形状相同的数组存贮数值解的值

y[0] = y_0 # 设置初始值

for i in range( len(x) - 1 ):
    y[i+1] = y[i] + h * dy(y[i])
# 计算数值解
######################################第一段代码演示结束


######################第二段代码演示开始
h = step length # 求解步长

a = 0
b = t_0
# 求解区间

t = np.arange(a, b+h, h)# 在求解区间内间隔 h 取点作为 t 数组

x = np.zeros(t.shape)
y = np.zeros(t.shape)
# 定义和 t 形状相同的数组存贮数值解的值

x[0]=x_0 
y[0]=y_0
# 设置初始值

for i in range( len(t) - 1 ):
    x[i+1]=x[i]+F_1(x[i],y[i])*h
    y[i+1]=y[i]+F_2(x[i],y[i])*h
# 计算数值解
######################################第二段代码演示结束

######################第二段代码演示开始
h = step length # 求解步长

a = 0
b = t_0
# 求解区间

t = np.arange(a, b+h, h)# 在求解区间内间隔 h 取点作为 t 数组

x = np.zeros(t.shape)
y = np.zeros(t.shape)
z = np.zeros(t.shape)
# 定义和 t 形状相同的数组存贮数值解的值

x[0]=x_0 
y[0]=y_0
z[0]=z_0
# 设置初始值

for i in range( len(t) - 1 ):
    x[i+1]=x[i]+F_1(x[i],y[i],z[i])*h
    y[i+1]=y[i]+F_2(x[i],y[i],z[i])*h
    z[i+1]=z[i]+F_3(x[i],y[i],z[i])*h
# 计算数值解
######################################第二段代码演示结束