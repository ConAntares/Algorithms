#### Visualization in 2D ####
### Elementary Plot ###

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sympy
from Luke_Color import *

# Global Setting
plt.rcParams['font.family'] = 'CMU Serif'        # Require CMU Serif font file. If not found, clear /home/luke/.cache/matplotlib
plt.rcParams['font.size'] = '14'                # Font Size
plt.rcParams['mathtext.fontset'] = 'cm'         # cm: Computer Mathematics
plt.rcParams['mathtext.rm'] = 'CMU Serif'        # Require CMU Serif font file
#plt.rcParams['text.usetex'] = True              # Require TeX environment
formatter = mpl.ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1))

fig, ax = plt.subplots(figsize=(8,6))
fig.suptitle('SupTitle', size='18', color='black')

x = np.linspace(-10,20,1000)
y = x**3+5*x**2+10
z = 3*x**2+10*x
a = 6*x+10
g = 100*np.sin(50*x)*np.exp(-x**2)+200
m = x**3-30*x
n = x**4

ax.set_title("SubTitle", size=16, color='black')

# Line
ax.plot(x, y, label="y(x)",color=myGold)
ax.plot(x, z, label="z(x)",color=myRed)
line,=ax.plot(x, a, label='a(x)',color=myOrange); line.set_dashes([1,1])
line,=ax.plot(x, g, alpha=1.0,label='Gaussian(x)',color=myGreen); line.set_dashes([1,0])
ax.plot(x, m, label="m(x)",color=myBlue)
ax.plot(x, n, label="n(x)",color=myPurple)

# Load Data
x, y = np.loadtxt('04 Visualization/data01.dat', unpack=True)
line,=plt.plot(20*x-5, 1000*y, antialiased=True,label='Data',color=myViolet); line.set_dashes([1,0])

# Text label
ax.text(0, 800, "Text label", fontsize=14, family="cmr10",bbox=dict(boxstyle='round',ec=(0.84,0.84,0.84,0.5),fc=(1.0,1.0,1.0,0.5)))

# Annotation
ax.plot(1, 0, "o")
ax.annotate("Annotation",fontsize=14, family="cmr10",xy=(1, 0), xycoords="data",xytext=(+10, +100), textcoords="offset points", arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-0.5"))

ax.grid(True, linestyle='--', color='#C8C8C8')                  # Grid
ax.legend(loc='best')                                          # Label
#ax.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.0)   # Label (outside)
ax.set(xlabel="X-Axis $x$")                                     # X-Axis Label
ax.set(ylabel="Y-Axis $y=f(x)$")                                # X-Axis Label
plt.xlim(-5, 11)
plt.ylim(-100, 1100)
plt.xticks([-4,-2,0,2,4,6,8,10], ['$-4$','$-2$','$0$','$2$','$4$','$6$','$8$','$10$'])
plt.yticks([0,200,400,600,800,1000], ['$0$','$200$','$400$','$600$','$800$','$1.0×10^3$'])
#ax.xaxis.set_major_formatter(formatter)                        # Scientific Counting Method: If you use this, Please close plt.xticks
#ax.yaxis.set_major_formatter(formatter)                        # Scientific Counting Method: If you use this, Please close plt.xticks
ax.set_axisbelow(True)
ax.tick_params(direction='in', top=True, right=True, bottom=True, left=True, which='both')
#mpl.ticker.LogLocator()

fig.savefig("2D Elementary Plot Py.pdf", dpi=1080)
plt.show()

### More Information ###
# https://matplotlib.org