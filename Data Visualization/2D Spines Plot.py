### Spines Plot ###

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

fig, ax = plt.subplots(figsize=(8,6))
fig.suptitle('Spines Plot SupTitle', size=18, color='black')
ax.set_title("Spines Plot SubTitle", size=16, color='black')

x = np.linspace(-10, 10, 500)
y = np.sin(x)/x

ax.plot(x, y)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
ticks=ax.set_xticks([-8,-4,0,4,8])
labels=ax.set_xticklabels(['$-8$','$-4$','$0$','$4$','$8$']) 
ax.set_yticks([0.5,1])
plt.setp(ax.xaxis.get_majorticklabels(),ha='left',va='top',rotation=10) 
plt.setp(ax.yaxis.get_majorticklabels(),ha='left',va='top',rotation=10) 


for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='gray', edgecolor='None', alpha=0.65 ))

#ax.grid(True, linestyle='--', color='#C8C8C8')
ax.set_axisbelow(True)
ax.tick_params(direction='in',which='both')
mpl.ticker.LogLocator()

fig.savefig("2D Spines Plot Py.pdf", dpi=1080)
plt.show()

### More Information ###
# https://matplotlib.org/