import random
from numpy import linalg as LA
import matplotlib.pyplot as plt

import numpy as np

M = 2
N = 2
K = 10000
p = np.array([0.5, 0.5])
m1 = np.array([2, 1])
m2 = np.array([-1, 1])
C1 = np.array([
    [3.0, -1.0],
    [-1.0, 3.0]
])
C2 = np.array([
    [5.0, 2.0],
    [2.0, 6.0]
])
C1_1 = LA.inv(C1)
C2_1 = LA.inv(C2)


lo = p[1] / p[0]
lo_ = np.log(lo)
x_1mass = []
y_1mass = []
x_2mass = []
y_2mass = []


for i in range(K):
    x = np.array([random.random() * 20 - 10, random.random() * 20 - 10])
    g__ = -0.5 * x.transpose().dot(C1_1 - C2_1).dot(x) + x.transpose().dot(C1_1.dot(m1) - C2_1.dot(m2)) - 0.5 * m1.transpose().dot(C1_1).dot(m1) + 0.5 * m2.transpose().dot(C2_1).dot(m2) - 0.5 * np.log(LA.det(C1) / LA.det(C2))
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


ax.scatter(x_1mass, y_1mass,
           c=[[0.1, 0.63, 0.55]],
           s=1)

ax.scatter(x_2mass, y_2mass,
           c='#ad09a3',
           s=1)


ax.set_facecolor('black')
ax.set_title('Один цвет')


fig.set_figwidth(14)
fig.set_figheight(14)

plt.show()