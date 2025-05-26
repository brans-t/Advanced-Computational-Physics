# Verlet-algorithm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp


def verlet(r, v, h, number):
    if len(r) == None:
        return 1
    else:
        r_x = r[:, 0]
        r_y = r[:, 1]
        v_x = v[:, 0]
        v_y = v[:, 1]
        print(v_x, v_y)
        a_x, a_y = force(r, number - 1)
        b_x, b_y = force(r, number)
        print(a_y, b_y)
        r_x = r_x + h * v_x + (a_x * (h ** 2)) / (2 * m)
        v_x = v_x + h * (a_x + b_x) / (2 * m)
        r_y = r_y + h * v_y + (a_y * (h ** 2)) / (2 * m)
        v_y = v_y + h * (a_y + b_y) / (2 * m)

    return r_x, r_y, v_x, v_y


def force(r, number):
    if len(r) == None:
        return 1
    else:
        f_x = 0
        f_y = -9.8  # 力
    return f_x, f_y


# 初始值
number = 10
dim = 2
h = 0.001
step = 10000

m = 10
x = []
y = []

r = np.random.rand(number, dim)

v = np.random.rand(number, dim)

for i in range(step):
    r_x,r_y,v_x,v_y = verlet(r,v,h,number)
    x.append(r_x)
    y.append(r_y)
    r[:,0] = r_x
    r[:,1] = r_y
    v[:,0] = v_x
    v[:,1] = v_y

# 绘图
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
