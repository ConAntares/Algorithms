#### Fibonacci Sequence

"""
f(n) =  1                   (n = 1)
        1                   (n = 2)
        f(n-1) + f(n-2)     (n > 2)
"""

#%%  Fibonacci With Iteration

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
print("Fibonacci With Iteration: The time interval is %f s." %td)

#%%  Fibonacci With Recursion

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
print("Fibonacci With Recursion: The time interval is %f s." %td)

#%%  Fibonacci Sequence in Array

to = time.time()

upLim = 40
N = np.arange(1,upLim+1,1)
M = np.array(list(map(fib,N)))

td = time.time() - to
print("Fibonacci Sequence in Array: The time interval is %f s." %td)

#%% Fibonacci with Iterator

to = time.time()
# upLim = 20
class Fibs:
    def __init__(self):
        self.c = 0
        self.a = 0
        self.b = 1
        self.n = upLim
    def __iter__(self):
        return self
    def __next__(self):
        self.i = self.a
        self.a = self.b
        self.b = self.i + self.b
        self.c = self.c + 1
        if self.c > self.n:
            raise StopIteration
        return self.a

fibs = Fibs()
td = time.time() - to
print("Fibonacci with Iterator: The time interval is %f s." %td)

P = np.array(list(fibs))
T = np.arange(1, upLim+1)
print(P)
print(T)

#%%  Plot

upLim = 40
N = np.arange(1,upLim+1,1)
M = np.array(list(map(fib,N)))

plt.rcParams['font.family'] = 'CMU Serif'
plt.rcParams['text.usetex'] = True
fig, ax = plt.subplots(1, 1)
plt.plot(N, M, c="#00B4DC", alpha=0.9)
plt.tick_params(direction='in')

plt.show()