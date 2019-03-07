# Calculate π using Taylor Series

import time

o = time.time()
s = 0.0
n = 0

for n in range(10000001):
    s = s + (-1)**n/(2*n+1)

pi = 4*s
t = time.time()

print(pi)
print("Time Interval:",t-o,"second")