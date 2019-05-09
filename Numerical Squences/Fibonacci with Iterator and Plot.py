#### Fibonacci Sequence with Iterator

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

P = np.array(list(fibs))
T = np.arange(1, upLim + 1)

plt.rcParams['font.family'] = 'CMU Serif'
plt.rcParams['text.usetex'] = True
fig, ax = plt.subplots(1, 1)
plt.plot(T, P, c="#00B4DC", alpha=0.9)
plt.tick_params(direction='in')

td = time.time() - to
print("Fibonacci with Iterator: The time interval is %f s." %td)

plt.show()