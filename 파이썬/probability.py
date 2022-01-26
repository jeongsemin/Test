from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

n = 10
p = 0.5

i_values = list(range(n+1))

dist = [binom.pmf(i,n,p) for i in i_values]
mean, var = binom.stats(n,p)

plt.bar(i_values, dist)
plt.show()