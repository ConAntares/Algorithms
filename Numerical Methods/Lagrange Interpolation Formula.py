#### Lagrange Interpolation Formula

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

def lagrange_interpolate(x, y, t):
    p = lagrange(x, y)
    u = p(t)

    plt.plot(x, y, "bo")
    plt.plot(t, u, "ro")
    plt.show()

x, y = np.loadtxt('Numerical Methods/Data/data02.dat', unpack=True)
t = np.linspace(1, 2, 10)
lagrange_interpolate(x, y, t)