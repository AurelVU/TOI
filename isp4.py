import numpy as np

from scipy.stats import norm


gamma = 0.07
K = 1000
t = norm.ppf((2 - gamma) / 2)
dg = t / (2 * np.sqrt(K))
print(dg)
