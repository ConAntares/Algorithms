import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['grid.color'] = '#DCDCDC'
rcParams['grid.linestyle'] = 'dashed'

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)

ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.set_proj_type('ortho')
    # 'ortho': Orthographic
    # 'persp': Perspective(default)
ax.set_axis_on()
ax.grid(True)

plt.show()


