#### Fibonacci Sequence with Array and Plo

"""
f(n) =  1                   (n = 1)
        1                   (n = 2)
        f(n-1) + f(n-2)     (n > 2)
"""

import time
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import ticker

to = time.time()
upLim = 40

def fib(n):
    a = 1
    b = 1
    c = 1
    if n < 1:
        print("Please a positive integer.")
        return -1
    while (n-2) > 0:
        c = b + a
        a = b
        b = c
        n = n - 1
    return c

N = np.arange(1, upLim + 1, 1)
M = np.array(list(map(fib, N)))

plt.rcParams['font.family'] = 'CMU Serif'
plt.rcParams['text.usetex'] = True
fig, ax = plt.subplots(1, 1)
plt.plot(N, M, c="#00B4DC", alpha=0.9)
plt.tick_params(direction='in')

td = time.time() - to
print("Fibonacci with Iteration: The time interval is %f s." %td)

plt.show()