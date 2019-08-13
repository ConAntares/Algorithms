#### Richardson Extrapolation
# coding: utf-8

import numpy as np
import time
#import matplotlib.pyplot as plt

"""
Sn = 1 + 1/2^2 + 1/3^2 + 1/4^2 + ... + 1/n^2
lim(n->∞)Sn = π^2/6 ≈ 1.6449340668482264

R1(n) = ((n+1)*S(n+1)-n*S(n))/np.math.factorial(1)
R2(n) = ((n+2)^2*S(n+1)-2*(n+1)^2*S(n+1)+n^2*S(n))/np.math.factorial(2)
……
"""

to = time.time()

X,Y = np.loadtxt('Data/Td.dat', unpack=True)

count = len(X)

def RE1(Y):
    R1 = np.ones(count)
    for i in range(0, count - 1):
        if i < count - 1 :
            R1[i] = ((i+1)*Y[i+1]-i*Y[i])/np.math.factorial(1)
        else:
            R1[i] = 0
        i = i + 1
    return R1

def RE2(Y):
    R2 = np.ones(count)
    for i in range(0, count - 2):
        if i < count - 2 :
            R2[i] = ((i+2)**2*Y[i+2]-2*(i+1)**2*Y[i+1]+i**2*Y[i])/np.math.factorial(2)
        else:
            R2[i] = 0
        i = i + 1
    return R2

def RET(Y):
    R2 = np.ones(count)
    Rt = RE2(RE2(RE2(RE2(RE2(RE2(RE2(RE2(RE2(RE2(RE2(RE2(RE2(RE2(RE2(RE2(R2))))))))))))))))
    return Rt

U1 = RE1(Y)
U2 = RE2(Y)
U3 = RET(RET(RET(RET(RET(RET(RET(RET(RET(RET(RET(RET(RET(RET(RET(RET(U2))))))))))))))))

td = time.time() - to
print("The time interval is %f s." %td)

# plt.rcParams['font.family'] = 'CMU Serif'
# plt.plot(X, Y, "o", c="#B4B4B4", alpha=0.9)
# plt.plot(X[0:len(U1)-1], U1[0:len(U1)-1], c="#FF1E14", alpha=0.9)
# plt.plot(X[0:len(U1)-2], U2[0:len(U1)-2], c="#1978F0", alpha=0.9)
# plt.tick_params(direction='in')
# plt.show()