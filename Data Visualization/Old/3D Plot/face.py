from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf

fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(0, 6, 0.25)
Y = np.arange(0, 6, 0.25)
X, Y = np.meshgrid(X, Y)

Z1 = np.zeros_like(X)
Z2 = np.ones_like(X)

for i in range(len(X)):
  for j in range(len(X[0])):
    Z1[i,j] = 0.5*(erf((X[i,j]+Y[i,j]-4.5)*0.5)+1)
    Z2[i,j] = 0.5*(erf((-X[i,j]-Y[i,j]+4.5)*0.5)+1)


alpha = 0.5

surf1 = ax.plot_surface(X, Y, Z1, cstride=2, rstride=1, cmap=cm.Oranges, linewidth=0, antialiased=False, alpha=alpha)

surf2 = ax.plot_surface(X, Y, Z2, cstride=2, rstride=1, cmap=cm.Blues, linewidth=0, antialiased=False, alpha=alpha)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf1, shrink=0.5, aspect=5)
fig.colorbar(surf2, shrink=0.5, aspect=5)

plt.show()
