import random
from numpy import linalg as LA
import matplotlib.pyplot as plt

import numpy as np

M = 2
N = 2
K = 10000
p = np.array([0.5, 0.5])
m = np.array([[2, 1], [-1, 1]])
C = np.array([
    [3.0, -1.0],
    [-1.0, 3.0]
])
C_1 = LA.inv(C)


lo = p[1] / p[0]
lo_ = np.log(lo)
x_1mass = []
y_1mass = []
x_2mass = []
y_2mass = []


for i in range(K):
    x = np.array([random.random() * 20 - 10, random.random() * 20 - 10])
    g__ = x.transpose().dot(C_1).dot(m[0] - m[1]) - 0.5 * (m[0] - m[1]).transpose().dot(C_1).dot(m[0] - m[1])
    print(x)

    if g__ < lo_:
        print('Первый класс')
        x_1mass.append(x[0])
        y_1mass.append(x[1])
    else:
        print('Второй класс')
        x_2mass.append(x[0])
        y_2mass.append(x[1])


fig, ax = plt.subplots()

# ключ цвета из {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}:
# RGB:
ax.scatter(x_1mass, y_1mass,
           c=[[0.1, 0.63, 0.55]],
           s=1)
# hex RGB:
ax.scatter(x_2mass, y_2mass,
           c='#ad09a3',
           s=1)


ax.set_facecolor('black')
ax.set_title('Один цвет')

#  Увеличим размер графика:
fig.set_figwidth(14)
fig.set_figheight(14)

plt.show()