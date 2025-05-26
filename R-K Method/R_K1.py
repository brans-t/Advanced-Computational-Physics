import matplotlib.pyplot as plt
import numpy as np
# 参数设置
x = []
y = []
rangee = 16              #区间
h = 0.2                  #步长
step = int(rangee/h)
# Rungen-Kutta
def K1(x,y):
    if x==None:
        return 1
    return y-2*x/y

def K2(x,y):
    if x==None:
        return 1
    return y+h/2*K1(x,y)-(2*x+h)/(y+h/2*K1(x,y))

def K3(x,y):
    if x==None:
        return 1
    return y+h/2*K2(x,y)-(2*x+h)/(y+h/2*K2(x,y))

def K4(x,y):
    if x==None:
        return 1
    return y+h*K3(x,y)-(2*(x+h))/(y+h*K3(x,y))
#初始条件
x_initial,y_initial=0,1
#主程序
for i in range(step+1):
    x.append(x_initial)
    y.append(y_initial)
    y_initial = y_initial + (h/6)*(K1(x_initial,y_initial)+2*K2(x_initial,y_initial)+2*K3(x_initial,y_initial)+K4(x_initial,y_initial))
    x_initial = rangee*(i+1)/step
#绘图
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

