import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib import rcParams
from Luke_Color import *

# Global Setting
plt.rcParams['font.family'] = 'CMU Serif'
#plt.rcParams['font.size'] = '14'               # Font Size
plt.rcParams['mathtext.fontset'] = 'cm'         # cm: Computer Mathematics
plt.rcParams['mathtext.rm'] = 'CMU Serif'       # Require CMU Serif font file
#plt.rcParams['grid.color'] = '#E1E1E1'
plt.rcParams['grid.color'] = '#F0F0F0'
plt.rcParams['grid.linestyle'] = 'solid'
plt.rcParams['text.usetex'] = True              # Require TeX environment
formatter = mpl.ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)

ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.set_proj_type('ortho')                   # 'ortho': Orthographic; 'persp': Perspective(default)
#ax.set_axis_off()
ax.set_axis_on()
ax.grid(True)

fig.savefig("3D Line Py.pdf", dpi=1080)
plt.show()

### More Information ###
# https://matplotlib.org