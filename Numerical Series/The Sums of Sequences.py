#### The Sums of Sequences

#  0. Time Interval Setting
import numpy as np
import time

#  1. Calculate e using Taylor Series

to = time.time()

s = 1.0
f = 1.0
for n in range(1,1001):
    f *= n
    s = s + 1/f
e = s

print("The natural logarithm is %f." %e)
td = time.time() - to
print("The time interval is %f s." %td)

#  2. Calculate π using Taylor Series

to = time.time()

s = 0.0
n = 0
for n in range(10000001):
    s = s + (-1)**n/(2*n+1)
pi = 4*s

print("The π is %f." %pi)
td = time.time() - to
print("The time interval is %f s." %td)

#  3. Calcute the sum(n!/n^n)

to = time.time()

s = 0
u = 1
d = 1
for n in np.arange(1,5,1):
    u = n * u           # n!
    d = n**n           # n^n
    s = s + u/d

print("The result of sum(n!/n^n) is %f" %s)
td = time.time() - to
print("The time interval is %f s." %td)