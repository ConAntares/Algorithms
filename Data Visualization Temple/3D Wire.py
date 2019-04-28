#### 3d Plot with Matplotlib in Python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from mpl_toolkits.mplot3d import axes3d
# from Luke_Color import *

## Global Setting

plt.rcParams['font.size']           = '12'
plt.rcParams['grid.color']          = '#D4D4D4'
plt.rcParams['grid.linestyle']      = 'dashed'
plt.rcParams['text.usetex']         = True 

formatter = mpl.ticker.ScalarFormatter(useMathText = True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1))

## Plot Statement

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

## Data Input

X, Y, Z = axes3d.get_test_data(0.05)

ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

## Ticks and Axes

ax.xaxis._axinfo['tick']['inward_factor'] = 0.0
ax.xaxis._axinfo['tick']['outward_factor'] = 0.2
ax.yaxis._axinfo['tick']['inward_factor'] = 0.0
ax.yaxis._axinfo['tick']['outward_factor'] = 0.2
ax.zaxis._axinfo['tick']['inward_factor'] = 0.0
ax.zaxis._axinfo['tick']['outward_factor'] = 0.2

ax.xaxis.pane.set_edgecolor('#D0D0D0')
ax.yaxis.pane.set_edgecolor('#D0D0D0')
ax.zaxis.pane.set_edgecolor('#D0D0D0')
ax.xaxis.pane.set_alpha(1)
ax.yaxis.pane.set_alpha(1)
ax.zaxis.pane.set_alpha(1)

ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.invert_xaxis()
ax.invert_yaxis()
ax.invert_zaxis()

ax.set_proj_type('persp')                   # 'ortho': Orthographic; 'persp': Perspective(default)
ax.grid(True)
ax.set_axis_on()

## Output

fig.savefig("3D Wire.pdf", dpi=1080)
plt.show()

## More Information

# https://matplotlib.org