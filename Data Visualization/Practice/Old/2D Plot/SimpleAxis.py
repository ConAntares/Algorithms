import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot

fig = plt.figure(8, (8, 6))
#fig, ax = plt.subplots()

ax = Subplot(fig, 111)
fig.add_subplot(ax)

ax.axis["right"].set_visible(True)
ax.axis["top"].set_visible(True)

plt.show()
