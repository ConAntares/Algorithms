import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d as mp3d

a = np.array([( 0, 0, 0),( 1, 0, 0),( 1, 1, 0),( 0, 1, 0)])
R1 = np.array([[0,-1,0],[1,0,0],[0,0,1]])
R2 = (R1[::-1].T)[:,[1,0,2]]
R3 = (R1[::-1])[:,[1,0,2]]
f = lambda a,r: np.matmul(r, a.T).T
g = lambda a,r: [a, f(a,r), f(f(a,r),r), f(f(f(a,r),r),r)]

fig = plt.figure()
ax = fig.add_subplot(111, projection=Axes3D.name)
ax.scatter([-1,1], [-1,1], [-1,1], alpha=0.0)

for i, ind , r in zip(range(3),[[0,1,2],[2,0,1],[1,2,0]], [R1,R2,R3]):
    xy = g(a[:,ind], r )
    for x in xy:
        face1 = mp3d.art3d.Poly3DCollection([x] , alpha=0.5, linewidth=1)
        face1.set_facecolor((i//2, i%2, i==0,  0.5))
        ax.add_collection3d(face1)

ax.grid(True)
ax.w_xaxis.pane.fill = False
ax.w_yaxis.pane.fill = False
ax.w_zaxis.pane.fill = False
plt.show()
