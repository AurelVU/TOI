from math import ceil
from scipy.stats import norm


P_err = 0.1
P_c = 1 - P_err
dg = 0.1 * P_err
gamma = 0.07

t = norm.ppf((2 - gamma) / 2)

K = ceil(t ** 2 * P_c * (1 - P_c) / dg ** 2)
print(K)
