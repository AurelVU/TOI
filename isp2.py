import numpy as np

from scipy.stats import norm


P_err = 0.1  # P_err = 1 - Pc
gamma = 0.07
K = 1000
t = norm.ppf((2 - gamma) / 2)
dg = t * np.sqrt(((1 - P_err) * P_err) / K)
print(dg)
