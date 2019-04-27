#### Fibonacci Sequence

"""
f(n) =  1                   (n = 1)
        1                   (n = 2)
        f(n-1) + f(n-2)     (n > 2)
"""

## With Iteration

import time
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import ticker

number = int(input("Please input a positive integer. \n"))
to = time.time()

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

re = fib(number)
if re != -1:
    print("The fibonacci sequence of %d is %d." %(number,re))
tf = time.time()
td = tf - to
print("The time interval is %f s." %td)

## With Recursion

number = int(input("Please input a positive integer. \n"))
to = time.time()

def fib_r(n):
    if n < 1:
        print("Please a positive integer.")
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fib_r(n-1) + fib_r(n-2)

re = fib_r(number)
if re != -1:
    print("The fibonacci sequence of %d is %d." %(number,re))
tf = time.time()
td = tf - to
print("The time interval is %f s." %td)

## Fibonacci Sequence in Array

to = time.time()

N = np.arange(1,101,1)
M = np.array(list(map(fib,N)))

td = time.time() - to
print("The time interval is %f s." %td)

fig, ax = plt.subplots(1, 1)
## Scientific Notation in Matplotlib
# formatter = ticker.ScalarFormatter(useMathText=True) 
# formatter.set_scientific(False)
# formatter.set_powerlimits((-1,1))
# ax.yaxis.set_major_formatter(formatter) 
plt.rcParams['font.family'] = 'CMU Serif'
plt.semilogy(N, M, c="#00B4DC", alpha=0.9)
plt.tick_params(direction='in')

plt.show()