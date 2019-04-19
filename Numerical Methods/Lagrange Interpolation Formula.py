#### Lagrange Interpolation Formula

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

def lagrange_interpolate(x, y, t):
    p = lagrange(x, y)
    return p(t)

x, y = np.loadtxt('Numerical Methods/Data/data02.dat', unpack=True)
t = np.linspace(1, 2, 10)
u = lagrange_interpolate(x, y, t)

plt.rcParams['font.family'] = 'CMU Serif'
plt.plot(t, u, "P", c="#00B4DC", alpha=0.9)
plt.plot(x, y, "o", c="#32B432", alpha=0.9)
plt.tick_params(direction='in')
plt.show()