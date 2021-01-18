from statistics import NormalDist
import numpy as np
from numpy import linalg as LA

pw1 = 0.6
pw2 = 0.4

m1 = np.array([2, 1, -1]).transpose()
m2 = np.array([2, -1, 2]).transpose()

C1 = np.array([
    [2, -0.5, -0.3],
    [-0.5, 1, -0.5],
    [-0.3, -0.5, 1]
])

C2 = np.array([
    [1, -0.3, -0.3],
    [-0.3, 1, -0.3],
    [-0.3, -0.3, 1]
])

C1_1 = LA.inv(C1)
C2_1 = LA.inv(C2)

mg1 = 0.5 * np.trace(C2_1.dot(C1) - np.eye(C1.shape[0])) + 0.5 * (m1 - m2).transpose().dot(C1_1).dot(m1 - m2) - 0.5 * np.log(LA.det(C1) / LA.det(C2))
h1 = mg1
Dg1 = 0.5 * np.trace((C2_1.dot(C1) - np.eye(C1.shape[0])) ** 2) + (m1 - m2).transpose().dot(C2_1).dot(C1).dot(C2_1).dot(m1 - m2)
d1 = Dg1
mg2 = 0.5 * np.trace(np.eye(C1.shape[0]) - C1_1.dot(C2)) - 0.5 * (m1 - m2).transpose().dot(C2_1).dot(m1 - m2) + 0.5 * np.log(LA.det(C2) / LA.det(C1))
h2 = mg2
Dg2 = 0.5 * np.trace((np.eye(C1.shape[0]) - C1_1.dot(C2)) ** 2) + (m1 - m2).transpose().dot(C1_1).dot(C2).dot(C1_1).dot(m1 - m2)
d2 = Dg2

l0 = pw2 / pw1
l0_ = np.log(l0)
print('Ошибка 1 рода:')
print(NormalDist().cdf((l0_ - mg1) / np.sqrt(Dg1)))
print('Ошибка 2 рода:')
print(1 - NormalDist().cdf((l0_ - mg2) / np.sqrt(Dg2)))
print('Суммарная ошибка:')
print(pw1 * NormalDist().cdf((l0_ - mg1) / np.sqrt(Dg1)) + pw2 * (1 - NormalDist().cdf((l0_ - mg2) / np.sqrt(Dg2))))
