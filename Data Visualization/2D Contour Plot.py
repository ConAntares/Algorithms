#### Visualization in 2D ####
### Contour Plot ###

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sympy
from Luke_Color import *
from matplotlib.colors import LinearSegmentedColormap

# Global Setting
plt.rcParams['font.family'] = 'CMU Serif'           # Require CMU Serif font file: cmr10.tff
plt.rcParams['font.size'] = '14'                # Font Size
plt.rcParams['mathtext.fontset'] = 'cm'         # cm: Computer Mathematics
plt.rcParams['mathtext.rm'] = 'CMU Serif'           # Require CMU Serif font file: cmr10.tff
plt.rcParams['text.usetex'] = True              # Require TeX environment
formatter = mpl.ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1))

## Figure
fig, ax = plt.subplots(figsize=(8,6))
fig.suptitle('SubTitle', size=18, color='black')
ax.set_title("SubTitle", size=16, color='black')

## Function
# x = np.linspace(-5, 5, 400)
# y = np.linspace(-5, 5, 400)
# X,Y = np.meshgrid(x,y)
# Z = np.cos(X)*np.cos(Y)*np.exp(-(X/5)**2-(Y/5)**2)

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2+Y**2)
Z = np.sin(4*R)/R

## Ploting
norm = mpl.colors.Normalize(-abs(Z).max(), abs(Z).max())
ContourPlot = ax.pcolor(X, Y, Z, norm=norm, cmap=ircac1)

ax.axis('tight')
ax.set_xlabel("X Axis: $x$", fontsize=18)
ax.set_ylabel("Y Axis: $y$", fontsize=18)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(4))
ax.yaxis.set_major_locator(mpl.ticker.MaxNLocator(4))
ax.tick_params(direction='in',which='both')

cbar = fig.colorbar(ContourPlot, ax=ax)
cbar.set_label("Color Map: $z$", fontsize=18)
#cbar.set_ticks([-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8])
cbar.outline.set_visible(True)
cbar.ax.tick_params(direction='in',right=True, left=True)

#mpl.ticker.LogLocator()

fig.savefig("2D Contour Py.pdf", dpi=1080)
#fig.savefig("2D Contour Py.png", dpi=1080)
plt.show()

### More Information ###
# Matplotlib:   https://matplotlib.org
# Color Map:    https://matplotlib.org/tutorials/colors/colormaps.html