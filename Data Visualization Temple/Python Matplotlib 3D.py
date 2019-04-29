#### 3D Plot with Matplotlib in Python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
# from IRCA import *

## Global Setting

plt.rc("font", **{"size":14,"family":"serif","serif":["Computer Modern"]})
plt.rc("text", usetex = True)

plt.rcParams["grid.color"]          = "#D4D4D4"
plt.rcParams["grid.linestyle"]      = "dashed"

formatter = mpl.ticker.ScalarFormatter(useMathText = True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1))

## Plot Statement

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

## Title

fig.suptitle(r"SupTitle with \LaTeX", size=18, color="black")
ax.set_title(r"SubTitle with \LaTeX", size=16, color="black")

## Data Input

x, y, z = np.loadtxt("Data/dataTov.dat", unpack=True)
surf = ax.plot_trisurf(x, y, z, cmap="gnuplot", antialiased=False)

## Ticks and Axes

ax.xaxis._axinfo["tick"]["inward_factor"] = 0.0
ax.xaxis._axinfo["tick"]["outward_factor"] = 0.2
ax.yaxis._axinfo["tick"]["inward_factor"] = 0.0
ax.yaxis._axinfo["tick"]["outward_factor"] = 0.2
ax.zaxis._axinfo["tick"]["inward_factor"] = 0.0
ax.zaxis._axinfo["tick"]["outward_factor"] = 0.2

ax.xaxis.pane.set_edgecolor("#D0D0D0")
ax.yaxis.pane.set_edgecolor("#D0D0D0")
ax.zaxis.pane.set_edgecolor("#D0D0D0")
ax.xaxis.pane.set_alpha(1)
ax.yaxis.pane.set_alpha(1)
ax.zaxis.pane.set_alpha(1)

ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.invert_xaxis()
ax.invert_yaxis()
ax.invert_zaxis()

ax.set_proj_type("persp")                   # "ortho": Orthographic; "persp": Perspective(default)
ax.grid(True)
ax.set_axis_on()

## Figure Output

# fig.savefig("Python Matplotlib 3D.pdf", dpi=512)
# fig.savefig("Python Matplotlib 3D.png", dpi=512)
plt.show()

## More Information

# https://matplotlib.org