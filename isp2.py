import numpy as np

from math import ceil
from scipy.stats import norm

# Рассчитать гарантированное число испытаний (с округлением до ближайшего целого)
# для оценки вероятности ошибки при следующих исходных данных: d=0.01, gamma=0.07
# ВНИМАНИЕ!!! есть задача, где d дается в зависимости от P. Там формула элементарная,
# перемножить 2 числа. Думаю справитесь


P_err = 0.1 # P_err = 1 - Pc
gamma = 0.07
K = 1000
t = norm.ppf((2 - gamma) / 2)
#print(t)
#K = ceil(t ** 2 / (4 * dg ** 2))
dg = t * np.sqrt(((1 - P_err) * P_err) / K)
print(dg)
