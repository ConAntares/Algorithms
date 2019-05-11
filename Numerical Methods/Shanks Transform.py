#### Shanks Transform

import numpy as np
import matplotlib.pyplot as plt

"""
L[i] = (S[i]^2-S[i-1]*S[i+1])/(2*S[i]-S[i-1]-S[i+1])
"""

# Load Harmonic Series
X,Y = np.loadtxt('Data/Tr.dat', unpack=True)

count = len(X)

## L1
L1 = np.empty(count)
for i in range(0,count):
    if i > 0 and i < count-1:
        L1[i] = (Y[i]**2-Y[i-1]*Y[i+1])/(2*Y[i]-Y[i-1]-Y[i+1])
    else:
        L1[i] = 0
    i = i + 1

## L2
L2 = np.empty(count)
for i in range(0,count):
    if i > 0 and i < count-1:
        L2[i] = (L1[i]**2-L1[i-1]*L1[i+1])/(2*L1[i]-L1[i-1]-L1[i+1])
    else:
        L2[i] = 0
    i = i + 1

## L3
L3 = np.empty(count)
for i in range(0,count):
    if i > 0 and i < count - 1:
        L3[i] = (L2[i]**2-L2[i-1]*L2[i+1])/(2*L2[i]-L2[i-1]-L2[i+1])
    else:
        L3[i] = 0
    i = i + 1

## L4
L4 = np.empty(count)
for i in range(0,count):
    if i > 0 and i < count - 1:
        L4[i] = (L3[i]**2-L3[i-1]*L3[i+1])/(2*L3[i]-L3[i-1]-L3[i+1])
    else:
        L4[i] = 0     
    i = i + 1

plt.rcParams['font.family'] = 'CMU Serif'
plt.plot(X, Y, "o", c="#B4B4B4", alpha=0.9)
plt.plot(X[1:len(L1)-1], L1[1:len(L1)-1], c="#F0140A", alpha=0.9)
plt.plot(X[2:len(L1)-2], L2[2:len(L1)-2], c="#FFC814", alpha=0.9)
plt.plot(X[3:len(L1)-3], L3[3:len(L1)-3], c="#00A0DC", alpha=0.9)
plt.plot(X[4:len(L1)-4], L2[4:len(L1)-4], c="#A064DC", alpha=0.9)

plt.tick_params(direction='in')
plt.show()