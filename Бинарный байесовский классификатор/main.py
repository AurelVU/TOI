import random
from numpy import linalg as LA
import matplotlib.pyplot as plt

import numpy as np

def print_word(a):
    for i in range(7):
        cur_str = ''
        for j in range(5):
            cur_str += '■' if a[i][j] == 1 else ' '
        print(cur_str)
    print('=====')

K_Word = np.array(
    [
        [1, 0, 0, 0, 1],
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 0, 1],
    ]
)

print_word(K_Word)

S_Word = np.array(
    [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
    ]
)
p = [0.5, 0.5]
lo = p[1] / p[0]
lo_ = np.log(lo)

print_word(S_Word)
pi = 0.1
if pi == 0:
    pi = 0.00000001
if pi == 0.5:
    pi = 0.49999999

p = np.array([1 - pi if K_Word[i // 5][i % 5] == 1 else pi for i in range(K_Word.size)])
q = np.array([1 - pi if S_Word[i // 5][i % 5] == 1 else pi for i in range(S_Word.size)])


x1 = np.array([[0] * 5] * 7)
for i in range(7):
    for j in range(5):
        if random.random() < pi:
            x1[i][j] = 1 - K_Word[i][j]
        else:
            x1[i][j] = K_Word[i][j]
print_word(x1)
g__ = 0
for i in range(7):
    for j in range(5):
        g__ += x1[i][j] * np.log(p[i * 5 + j] / q[i * 5 + j]) + (1 - x1[i][j]) * np.log((1 - p[i * 5 + j]) / (1 - q[i * 5 + j]))

if g__ > lo_:
    print("ЭТО БУКВА К!!!")
else:
    print("ЭТО БУКВА S!!!")

x2 = np.array([[0] * 5] * 7)
for i in range(7):
    for j in range(5):
        if random.random() < pi:
            x2[i][j] = 1 - S_Word[i][j]
        else:
            x2[i][j] = S_Word[i][j]
print_word(x2)
g__ = 0
for i in range(7):
    for j in range(5):
        g__ += x2[i][j] * np.log(p[i * 5 + j] / q[i * 5 + j]) + (1 - x2[i][j]) * np.log((1 - p[i * 5 + j]) / (1 - q[i * 5 + j]))

if g__ > lo_:
    print("ЭТО БУКВА К!!!")
else:
    print("ЭТО БУКВА S!!!")
