#### Visualization in 2D ####
### Multiple Plot ###

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

fig, ax = plt.subplots(2,2,figsize=(12,8),constrained_layout=True)
ax = ax.flatten()
fig.suptitle('SupTitle', size='18', color='black')

x = np.linspace(-2*np.pi, 2*np.pi,1000)
y = np.sin(x*np.pi*6)*np.exp(-(2*x)**2)*0.2*np.pi
a = np.linspace(-10,10,1000)

## Fig[1,1]: axes[0]
ax[0].set_title('Title of Subplot 1')

line,=ax[0].plot(x, y, label='Linear'); line.set_dashes([1,1])
ax[0].text(0,0,'Text',size=16,rotation=0,ha='center',va='center')

ax[0].grid(True, linestyle='--', color='#C8C8C8', which='both')  
ax[0].set_xlim(-1, 1)
ax[0].set_ylim(-1, 1)
ticks=ax[0].set_xticks([-0.8,-0.4,0,0.4,0.8])
labels=ax[0].set_xticklabels(['$-0.8$','$-0.4$','$0$','$0.4$','$0.8$'], rotation=10,) 
ticks=ax[0].set_yticks([-0.8,-0.4,0,0.4,0.8])
labels=ax[0].set_yticklabels(['$-0.8$','$-0.4$','$0$','$0.4$','$0.8$'], rotation=10,) 
#ax[0].xaxis.set_major_formatter(formatter)
#ax[0].yaxis.set_major_formatter(formatter)
ax[0].set_axisbelow(True)
ax[0].tick_params(direction='in', top=True, right=True, bottom=True, left=True, which='both')
ax[0].annotate('(a)',xy=(0.95, 0.05), xycoords='axes fraction',size=14,rotation=0,ha='center',va='center')

## Fig[1,2]: axes[1]
ax[1].set_title('Title of Subplot 2')

ax[1].semilogy(a, a**1, label='Linear')
ax[1].semilogy(a, a**2, label='Quadratic')
ax[1].semilogy(a, a**3, label='Cubic')

ax[1].legend(loc='best')
ax[1].set_xlim(-10, 10)
#ax[1].set_ylim(0, 10000)
ticks=ax[1].set_xticks([-8,-4,0,4,8])
labels=ax[1].set_xticklabels(['$-8$','$-4$','$0$','$4$','$8$'], rotation=10,) 
ax[1].tick_params(direction='in', top=True, right=True, bottom=True, left=True, which='both')
ax[1].annotate('(b)',xy=(0.95, 0.05), xycoords='axes fraction',size=14,rotation=0,ha='center',va='center',weight='bold')

## Fig[2,1]: axes[2]
ax[2].set_title('Title of Subplot 3')

line,=ax[2].plot(a, a**1,label='Linear'); line.set_dashes([2,1,1,1])
line,=ax[2].plot(a, a**2,label='Quadratic'); line.set_dashes([2,1,1,1])
line,=ax[2].plot((-1)*a, a**3,label='Cubic'); line.set_dashes([2,1,1,1])
ax[2].semilogy(a, a**(1/3),alpha=0.0)

ax[2].legend(loc='best')
ax[2].set_xlim(-10, 10)
#ax[2].set_ylim(0, 10000)
ticks=ax[2].set_xticks([-8,-4,0,4,8])
labels=ax[2].set_xticklabels(['$-8$','$-4$','$0$','$4$','$8$'], rotation=10,) 
ax[2].yaxis.set_major_formatter(formatter)
ax[2].tick_params(direction='in', top=True, right=True, bottom=True, left=True, which='both')
ax[2].annotate('(c)',xy=(0.95, 0.05), xycoords='axes fraction',size=14,rotation=0,ha='center',va='center')

## Fig[1,1]: axes[3]
ax[3].set_title('Title of Subplot 4')


line,=ax[3].plot(a, a**1,label='Linear'); line.set_dashes([2,1,1,1])
ax[3].loglog(a, a**1,alpha=0.0)

ax[3].tick_params(direction='in')
ax[3].annotate('(d)',xy=(0.95, 0.05), xycoords='axes fraction',size=14,rotation=0,ha='center',va='center')

fig.savefig("2D Multiple Plot Py.pdf", dpi=1080)
plt.show()

### More Information ###
# https://matplotlib.org/