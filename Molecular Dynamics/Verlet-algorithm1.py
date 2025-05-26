#Verlet-algorithm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp

def verlet(r,v,h,number):
    if len(r) == None:
        return 1
    else:
         print(r)
         a = force(r, number-1)
         r = r + h*v + (force(r, number)*(h**2))/(2*m)
         v = v + h*(force(r, number)+a)/(2*m)
    return r,v,a

def force(r, number):
    if len(r) == None:
        return 1
    else:
        f = 0             #力
    return f

#初始值
number = 10
dim = 2
h = 0.01
step = 1000

m = 1
x = []
y = []

r = np.random.rand(number, dim)
v = np.random.rand(number, dim)

for i in range(step):
    r,v,a = verlet(r,v,h,number)
    r_x = r[:,0]
    r_y = r[:,1]
    x.append(r_x)
    y.append(r_y)
    # print(r_x)

# 绘图
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

