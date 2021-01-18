from statistics import NormalDist
import numpy as np

# Рассчитать вероятность ошибки распознавания второго рода с
# использованием наивного байесовского классификатора для n признаков,
# распределенных по показательному закону (используйте стандартную функцию normcdf)
# pw1=0.5; pw2=0.5; n=100;
# L1=1; L2=1.5;


pw1 = 0.5
pw2 = 0.5
n = 100
l1 = 1
l2 = 1.5

mg1 = n * (np.log(l2 / l1) + l1 * (1 / l2 - 1 / l1))
Dg1 = n * (l1 ** 2 * (1 / l2 - 1 / l1) ** 2)
mg2 = n * (np.log(l2 / l1) + l2 * (1 / l2 - 1 / l1))
Dg2 = n * (l2 ** 2 * (1 / l2 - 1 / l1) ** 2)
l0 = pw1 / pw2
l0_ = np.log(l0)

print('Ошибка 1 рода:')
print(NormalDist(mu=mg1, sigma=np.sqrt(Dg1)).cdf(l0_))
print('Ошибка 2 рода:')
print(1 - NormalDist(mu=mg2, sigma=np.sqrt(Dg2)).cdf(l0_))
print('Суммарная ошибка:')
print(pw1 * NormalDist(mu=mg1, sigma=np.sqrt(Dg1)).cdf(l0_) + pw2 * (1 - NormalDist(mu=mg2, sigma=np.sqrt(Dg2)).cdf(l0_)))
