"""
Монету подбросили 144 раза.
Какова вероятность, что орел выпадет ровно 70 раз?
"""

import scipy.special as sc

p = 0.5
q = 0.5
n = 144
k = 70
pp = sc.comb(n, k) * p**k * q**(n-k)
print("вероятность, что орел выпадет ровно 70 раз ", pp)
# 0.06281178035144777
