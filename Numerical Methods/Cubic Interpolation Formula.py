#### Cubic Interpolation

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x, y = np.loadtxt('Data/cubic.dat', unpack=True)
t = np.linspace(0.01, 67, 100)

f = interp1d(x, y, kind='cubic')
u = f(t)

plt.rcParams['font.family'] = 'CMU Serif'
plt.plot(t, u,      c="#00B4DC", alpha=0.9)
plt.plot(x, y, "o", c="#32B432", alpha=0.9)
plt.tick_params(direction='in')
plt.show()