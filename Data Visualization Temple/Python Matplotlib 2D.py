#### 2D Plot with Matplotlib in Python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# from IRCA import *

## Global Setting

plt.rc("font", **{"size":14,"family":"serif","serif":["Computer Modern"]})
plt.rc("text", usetex = True)

formatter = mpl.ticker.ScalarFormatter(useMathText = True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1))

## Plot Statement

fig, ax = plt.subplots(figsize=(8,6))

## Title

fig.suptitle(r"SupTitle with $y=f(x)$", size=18, color="black")
ax.set_title(r"SubTitle with $y=f(x)$", size=16, color="black")

## Data Input

x, y = np.loadtxt("Data/data00.dat", unpack=True)
line,= plt.plot(x, y, color="#F0140A", lw=1.2, alpha=1, label = "Function 1", antialiased=True)
fill = ax.stackplot(x, y, color="#F0140A", alpha=0.25)

x, y = np.loadtxt("Data/data08.dat", unpack=True)
line,= plt.plot(x, y, color="#FFC814", lw=1.2, alpha=1, label = "Function 2", antialiased=True)
fill = ax.stackplot(x, y, color="#FFC814", alpha=0.25)

x, y = np.loadtxt("Data/data16.dat", unpack=True)
line,= plt.plot(x, y, color="#F0F000", lw=1.2, alpha=1, label = "Function 3", antialiased=True)
fill = ax.stackplot(x, y, color="#F0F000", alpha=0.25)

x, y = np.loadtxt("Data/data24.dat", unpack=True)
line,= plt.plot(x, y, color="#32B432", lw=1.2, alpha=1, label = "Function 4", antialiased=True)
fill = ax.stackplot(x, y, color="#32B432", alpha=0.25)

x, y = np.loadtxt("Data/data32.dat", unpack=True)
line,= plt.plot(x, y, color="#1978BE", lw=1.2, alpha=1, label = "Function 5", antialiased=True)
fill = ax.stackplot(x, y, color="#1978BE", alpha=0.25)

x, y = np.loadtxt("Data/data40.dat", unpack=True)
line,= plt.plot(x, y, color="#A064DC", lw=1.2, alpha=1, label = "Function 6", antialiased=True)
fill = ax.stackplot(x, y, color="#A064DC", alpha=0.25,baseline="zero")

## Legend and Axes Setting

ax.legend(loc='best')
ax.set(xlabel=r"X-Axis $x$")
ax.set(ylabel=r"Y-Axis $y=f(x)$") 

## Grids and Ticks Setting

ax.grid(True, linestyle="--", color="#D0D0D0", lw=1, alpha=0.5)
ax.tick_params(direction="in", top=True, right=True, bottom=True, left=True, which="both")
plt.xlim(-0.1, 4.1)
plt.ylim(-0.05, 2.05)

## Figure Output

# fig.savefig("Python Matplotlib 2D.pdf", dpi=512)
# fig.savefig("Python Matplotlib 2D.png", dpi=512)
plt.show()

## More Information

# https://matplotlib.org