#### Lagrange Interpolation Formula

import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

to = time.time()

def lagrange_interpolate(x, y, t):
    p = lagrange(x, y)
    return p(t)

x, y = np.loadtxt('Numerical Methods/Data/data02.dat', unpack=True)
t = np.linspace(1, 2, 11)
u = lagrange_interpolate(x, y, t)

td = time.time() - to
print("The time interval is %f s." %td)

plt.rcParams['font.family'] = 'CMU Serif'
plt.plot(t, u, "P", c="#00B4DC", alpha=0.9)
plt.plot(x, y, "o", c="#32B432", alpha=0.9)
plt.tick_params(direction='in')
plt.show()