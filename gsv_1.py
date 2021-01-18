from statistics import NormalDist
import numpy as np
from numpy import linalg as LA

pw1 = 0.1
pw2 = 0.9

m1 = np.array([2.0, 1.0, 2.0, 2.0, 1.0]).transpose()
m2 = np.array([1.0, -1.0, 1.0, -1.0, 1.0]).transpose()
C = np.array([
    [1.0, 0.1, 0, 0, 0],
    [0.1, 2.0, 0, 0, 0],
    [0, 0, 2.0, 0, 0],
    [0, 0, 0, 1.0, 0],
    [0, 0, 0, 0, 1.0]
])

# pw1 = 0.5
# pw2 = 0.5
# m1 = np.array([2, 1, -1]).transpose()
# m2 = np.array([2, -1, 2]).transpose()
#
# C = np.array(
#     [[2, -0.5, -0.3],
#      [-0.5, 1, -0.5],
#      [-0.3, -0.5, 1]]
# )

C_1 = LA.inv(C)

mg1 = (m1 - m2).transpose().dot(C_1).dot(m1 - m2) * 0.5
h = mg1
Dg1 = 2 * h
mg2 = -h
Dg2 = 2 * h

l0 = pw2 / pw1
l0_ = np.log(l0)
print('Ошибка 1 рода:')
print(NormalDist(mu=mg1, sigma=np.sqrt(Dg1)).cdf(l0_))
print('Ошибка 2 рода:')
print(1 - NormalDist(mu=mg2, sigma=np.sqrt(Dg2)).cdf(l0_))
print('Суммарная ошибка:')
print(pw1 * NormalDist(mu=mg1, sigma=np.sqrt(Dg1)).cdf(l0_) + pw2 * (1 - NormalDist(mu=mg2, sigma=np.sqrt(Dg2)).cdf(l0_)))
