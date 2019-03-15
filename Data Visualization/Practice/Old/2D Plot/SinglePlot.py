# Single Plot Template with Matplotlib in Python
import matplotlib as pl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import *

rcParams['font.family'] = 'CMU Serif'
rcParams['font.size'] = '12'
rcParams['mathtext.rm'] = 'CMU serif'
rcParams['mathtext.fontset'] = 'cm'
#rcParams['text.usetex'] = True
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,2))

fig, ax = plt.subplots(figsize=(8, 6))
fig.suptitle('SupTitle',size='18')
ax.annotate("Ammotate",xy=(0.2, 0.3), xycoords='figure fraction',size=16,rotation=0,ha="center",va="center",bbox=dict(boxstyle="round",ec=(0.84,0.84,0.84,0.5),fc=(1.0,1.0,1.0,0.5),))

x = np.linspace(1, 100, 10000)

line,=ax.plot(x, x**1, label='Linear')
line.set_dashes([1,1])
ax.plot(x, x**2, label='Quadratic')
ax.plot(x, x**3, label='Cubic')
#ax.semilogy(x, x**1, label='Linear')
#ax.semilogy(x, x**2, label='Quadratic')
#ax.semilogy(x, x**3, label='Cubic')
#x, y = np.loadtxt('test.dat', unpack=True)
#line,=plt.plot(x, y, color=Red, lw='1', alpha=1, antialiased=True) 
#line.set_dashes([1,1])

ax.text(10,100,"Text",size=16,rotation=0,ha="center",va="center",bbox=dict(boxstyle="round",ec=(0.84,0.84,0.84,0.5),fc=(1.0,1.0,1.0,0.5),))

#plt.xlim(0, 100)
#plt.ylim(0, 1000000)
ax.set(title='Title')
ax.set(xlabel='X-Axis $X-Axis\sum\phi{\phi}^2 $')
ax.set(ylabel='Y-Axis')
plt.xticks([0,20,40,60,80,100], ['$0$','$20$','$40$','$60$','$80$','$1.0$×$10^2$'])
#plt.yticks([], [])
ax.legend(loc='best')
    # bbox_to_anchor=(0.5, 0.5)
ax.grid(True,linestyle='--',color='#C8C8C8')
ax.set_axisbelow(True)
ax.tick_params(direction='in', top=True, right=True, bottom=True, left=True, which='both')
pl.ticker.LogLocator()
#ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

fig.savefig("SinglePlot.pdf")
plt.show()
