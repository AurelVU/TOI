import numpy as np
from scipy import stats

pw1 = 0.3
pw2 = 0.7
n = 5
p = 0.9  # p > q!  Если больше, то по идее можно просто поставить "-" при вычислении L0, но это не точно
q = 0.2

l0 = pw1 / pw2
l0_ = np.log(l0)
L0 = round((l0_ - n * np.log((1 - p) / (1 - q))) / np.log((p * (1 - q)) / (q * (1 - p))))

a = stats.binom.cdf(L0 - 1, n, p)
b = 1 - stats.binom.cdf(L0, n, q)
print('Ошибка 1 рода: ')
print(a)
print('Ошибка 2 рода: ')
print(b)
