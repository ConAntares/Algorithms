# Muti Plots Template with Matplotlib in Python
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
formatter.set_powerlimits((-1,1))

fig, ax = plt.subplots(nrows=2,ncols=2,figsize=(12, 8),constrained_layout=True)
ax = ax.flatten()
fig.suptitle('SupTitle',size='18')

x = np.linspace(1, 10, 100000)

line,=ax[0].plot(x, x**1, label='Linear')
line.set_dashes([1,1])
ax[0].set_title('Title of Subplot 0')
#ax[0].set_xlim(0, 1000)
#ax[0].set_ylim(0, 1000)
#ax[0].xaxis.set_major_formatter(formatter)
ax[0].yaxis.set_major_formatter(formatter)
ticks = ax[0].set_xticks([0,20,40,60,80,100])
labels = ax[0].set_xticklabels(['$0$','$20$','$40$','$60$','$80$','$10.0$×$10$'], rotation=0,)  
#ticks = ax[0].set_yticks([])
#labels = ax[0].set_yticklabels([])
ax[0].text(1,1,'Text',size=16,rotation=0,ha='center',va='center',bbox=dict(boxstyle='round',ec=(0.84,0.84,0.84,0.5),fc=(1.0,1.0,1.0,0.5),))
ax[0].annotate('(a)',xy=(0.95, 0.05), xycoords='axes fraction',size=14,rotation=0,ha='center',va='center')
ax[0].tick_params(direction='in', top=True, right=True, bottom=True, left=True, which='both')
pl.ticker.LogLocator()

ax[1].set_title('Title of Subplot 1')
line,=ax[1].plot(x, x**1, label='Linear')
line.set_dashes([1,0])
#ax[1].set_xlim(0, 1000)
#ax[1].set_ylim(0, 1000)
#ax[1].xaxis.set_major_formatter(formatter)
ax[1].yaxis.set_major_formatter(formatter)
ax[1].annotate('(b)',xy=(0.95, 0.05), xycoords='axes fraction',size=14,rotation=0,ha='center',va='center',weight='bold')
ax[1].tick_params(direction='in', top=True, right=True, bottom=True, left=True, which='both')
pl.ticker.LogLocator()

ax[2].set_title('Title of Subplot 2')
ax[2].annotate('(c)',xy=(0.95, 0.05), xycoords='axes fraction',size=14,rotation=0,ha='center',va='center')
ax[2].tick_params(direction='in', top=True, right=True, bottom=True, left=True, which='both')
pl.ticker.LogLocator()

ax[3].set_title('Title of Subplot 3')
ax[3].annotate('(d)',xy=(0.95, 0.05), xycoords='axes fraction',size=14,rotation=0,ha='center',va='center')
ax[3].tick_params(direction='in', top=True, right=True, bottom=True, left=True, which='both')
pl.ticker.LogLocator()


fig.savefig('MutiPlots.pdf')
plt.show()
