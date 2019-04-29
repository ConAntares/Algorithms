#### Factorial

import sys
import math
import time
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import ticker

sys.setrecursionlimit(10000)

## Factorial without Recursion

number = int(input("Please input a positive integer. \n"))
to = time.time()

def factorial(n):
    result = n
    for i in np.arange(1,n):
        result = result*i
    return result

re = factorial(number)
print("The factorial of %d is %d." %(number,re))
tf = time.time()
td = tf - to
print("The time interval is %f s." %td)

## Factorial with Recursion

number = int(input("Please input a positive integer. \n"))
to = time.time()

def factorial_r(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_r(n-1)

re = factorial_r(number)
print("The factorial of %d is %d." %(number,re))
tf = time.time()
td = tf - to
print("The time interval is %f s." %td)

# Factorial with math.factorial(x)

number = int(input("Please input a positive integer. \n"))
to = time.time()

re = math.factorial(number)
print("The factorial of %d is %d." %(number,re))
tf = time.time()
td = tf - to
print("The time interval is %f s." %td)

## Factorial in Array

to = time.time()

N = np.arange(1,41,1)
M = np.array(list(map(math.factorial,N)))

td = time.time() - to
print("The time interval is %f s." %td)

## Plot

plt.rcParams['font.family'] = 'CMU Serif'
plt.rcParams['text.usetex'] = True
fig, ax = plt.subplots(1, 1)
plt.plot(N, M, c="#00B4DC", alpha=0.9)
plt.tick_params(direction='in')

plt.show()