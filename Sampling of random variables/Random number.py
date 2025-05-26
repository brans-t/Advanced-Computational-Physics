import random
import numpy as np
def red_numbers(t):
    if t == None:
        return 1
    else:
        for i in range(6):
            t = random.choice(list1)
            red.append(t)
    return red

def blue_numbers(t):
    if t == None:
        return 1
    else:
        blue = random.choice(list2)
    return blue

red = []
blue = []

list1 = []
list2 = []
a = 1
for i in range(33):
    list1.append(a)
    a = a + 1

list2 = list1[:16]
#输出
print(f"The predicted number is: \nRed Ball Number:{red_numbers(1)}\nBlue Ball Number:[{blue_numbers(1)}]")
