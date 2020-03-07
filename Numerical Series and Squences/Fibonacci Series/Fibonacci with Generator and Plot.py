#### Fibonacci with Generator

import time
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import ticker

to = time.time()
upLim = 40

def libs():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a

count = 0
le = ([])
for each in libs():
    count += 1
    if count >= upLim:
        break
    le.append(each)
    print(each, end = " ")

print("\n")
print(le)

N = np.arange(1, count, 1)
M = le

plt.rcParams['font.family'] = 'CMU Serif'
plt.rcParams['text.usetex'] = True
fig, ax = plt.subplots(1, 1)
plt.plot(N, M, c="#00B4DC", alpha=0.9)
plt.tick_params(direction='in')

td = time.time() - to
print("Fibonacci with Iteration: The time interval is %f s." %td)

plt.show()
