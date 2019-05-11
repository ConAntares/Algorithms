#### Richardson Extrapolation

import numpy as np
import matplotlib.pyplot as plt

"""
Sn = 1 + 1/2^2 + 1/3^2 + 1/4^2 + ... + 1/n^2
lim(n->∞)Sn = π^2/6 ≈ 1.6449340668482264

R1(n) = ((n+1)*S(n+1) - n*S(n))/1!
R2(n) = ((n+2)^2*S(n+1)-2*(n+1)^2*S(n+1)+n^2*S(n))/2!
"""
