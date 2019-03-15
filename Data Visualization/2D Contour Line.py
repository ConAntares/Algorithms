#### Visualization in 2D ####
### Contour Line Plot ###

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np
import sympy
from Luke_Color import *

# Global Setting
plt.rcParams['font.family'] = 'CMU Serif'           # Require CMU Serif font file: cmr10.tff
plt.rcParams['font.size'] = '14'                # Font Size
plt.rcParams['mathtext.fontset'] = 'cm'         # cm: Computer Mathematics
plt.rcParams['mathtext.rm'] = 'CMU Serif'           # Require CMU Serif font file: cmr10.tff
plt.rcParams['text.usetex'] = True              # Require TeX environment
formatter = mpl.ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1))

fig, ax = plt.subplots(figsize=(8,6))
fig.suptitle('SupTitle', size=18, color='black')
ax.set_title("SubTitle", size=16, color='black')

## Function or Data
delta = 0.01
x = np.arange(-4.0, 4.0, delta)
y = np.arange(-4.0, 4.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2-Y**2)
Z2 = np.exp(-(X-1)**2-(Y-1)**2)
Z = (Z1-Z2)*2

CS = ax.contour(X, Y, Z ,cmap=ircal)
plt.clabel(CS, inline=1, fontsize=10)

fig.savefig("2D Contour Line Py.pdf", dpi=1080)
plt.show()

### More Information ###
# https://matplotlib.org