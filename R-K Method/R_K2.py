import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# Runge-Kutta algorithm ------------------------------------------------------------------------------------------------
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

def R_K(x,y):
    if x == None:
        return 1
    return y + (h / 6) * (K1(x, y) + 2 * K2(x, y) + 2 * K3(x, y) + K4(x, y))

    # Adams algorithm--------------------------------------------------------------------------------------------------------------------------------
def Adams(x_initial, i):
    if x_initial == None:
        return 1
    else:
        y_initial = y[i] + (h / 24) * (
                    55 * K1(x[i], y[i]) - 59 * K1(x[i - 1], y[i - 1]) + 37 * K1(x[i - 2], y[i - 2]) - 9 * K1(
                x[i - 3], y[i - 3]))
        m[i + 1] = y_initial + (251 / 270) * (c[i] - p[i])
        m[i + 1] = K1(x_initial, m[i + 1])
        c[i + 1] = y[i] + (h / 24) * (
                    9 * m[i + 1] + 19 * K1(x[i], y[i]) - 5 * K1(x[i - 1], y[i - 1]) + K1(x[i - 2], y[i - 2]))
        y_initial = c[i + 1] + (19 / 270) * (c[i + 1] - y_initial)

    return y_initial

rangee = 16
h = 0.1
step = int(rangee / h)
x_initial, y_initial = 0, 1

x = []
y = []
c = []
p = []
m = []
z = []

# 初值
for i in range(step + 1):
    x.append(x_initial)
    c.append(y_initial)
    p.append(y_initial)
    m.append(y_initial)
    y.append(y_initial)
    y_initial = R_K(x_initial, y_initial)
    x_initial = rangee * (i + 1) / step
x = x[:4]
y = y[:4]
c[3] = 0
p[3] = 0

# Adams algorithm-----------------------------------------------------------------------------------------------------------------
for i in range(3, step, 1):
    x_initial = x[i] + h
    y_initial = Adams(x_initial, i)
    x.append(x_initial)
    y.append(y_initial)

n = 1
for i in range(step + 1):
    z.append(n)
    m = (i + 1) / step
    n = math.sqrt(1 + 2 * m)

plt.plot(x, y, label=r"Adams")
plt.plot(x, z, label=r"Real")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
