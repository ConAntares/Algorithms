#### 2D Plot with Matplotlib in Python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# from IRCA import *

## Global Setting

plt.rc('font', **{'family':'serif','serif':['Computer Modern']})
plt.rc('text', usetex = True)

plt.rcParams['grid.color']          = '#D4D4D4'
plt.rcParams['grid.linestyle']      = 'dashed'

formatter = mpl.ticker.ScalarFormatter(useMathText = True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1))

## Plot Statement

fig, ax = plt.subplots(figsize=(8,6))

## Title

fig.suptitle(r"SupTitle with \LaTeX", size=18, color='black')
ax.set_title(r"SubTitle with \LaTeX", size=16, color='black')

## Data Input

x, y = np.loadtxt('Data/data00.dat', unpack=True)
line,= plt.plot(x, y, color='#F0140A', lw='1.2', alpha=1, antialiased=True)

x, y = np.loadtxt('Data/data08.dat', unpack=True)
line,= plt.plot(x, y, color='#FFC814', lw='1.2', alpha=1, antialiased=True)

x, y = np.loadtxt('Data/data16.dat', unpack=True)
line,= plt.plot(x, y, color='#F0F000', lw='1.2', alpha=1, antialiased=True)

x, y = np.loadtxt('Data/data24.dat', unpack=True)
line,= plt.plot(x, y, color='#32B432', lw='1.2', alpha=1, antialiased=True)

x, y = np.loadtxt('Data/data32.dat', unpack=True)
line,= plt.plot(x, y, color='#1978BE', lw='1.2', alpha=1, antialiased=True)

x, y = np.loadtxt('Data/data40.dat', unpack=True)
line,= plt.plot(x, y, color='#A064DC', lw='1.2', alpha=1, antialiased=True)

## Figure Output

# fig.savefig("Python Matplotlib 2D.pdf", dpi=1080)
plt.show()

## More Information

# https://matplotlib.org