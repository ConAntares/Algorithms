### Twin Axes ###

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sympy

# Global Setting
plt.rcParams['font.family'] = 'CMU Serif'           # Require CMU Serif font file: cmr10.tff
plt.rcParams['font.size'] = '14'                # Font Size
plt.rcParams['mathtext.fontset'] = 'cm'         # cm: Computer Mathematics
plt.rcParams['mathtext.rm'] = 'CMU Serif'           # Require CMU Serif font file: cmr10.tff
#plt.rcParams['text.usetex'] = True              # Require TeX environment
formatter = mpl.ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1))

fig, ax1 = plt.subplots(figsize=(8,6))
fig.suptitle('SupTitle', size='18', color='black')

# Line
r = np.linspace(0, 5, 100)
a = 4*np.pi*r**2
v = (4*np.pi/3)*r**3

ax1.set_title("surface area and volume of a sphere", fontsize=16)
ax1.set_xlabel("radius [m]", fontsize=16)

ax1.plot(r, a, color="blue")
ax1.set_ylabel(r"surface area ($m^2$)", fontsize=16, color="blue")
for label in ax1.get_yticklabels():
    label.set_color("blue")
ax1.tick_params(direction='in',which='both')

ax2 = ax1.twinx()
ax2.plot(r, v, color="red")
ax2.set_ylabel(r"volume ($m^3$)", fontsize=16, color="red")
for label in ax2.get_yticklabels():
    label.set_color("red")
ax2.tick_params(direction='in',which='both')

fig.savefig("2D Twin Axes Py.pdf", dpi=1080)
plt.show()

### More Information ###
# https://matplotlib.org/