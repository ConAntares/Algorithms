# Calculate e using Taylor Series

import time

o = time.time()
s = 1.0
f = 1.0

for n in range(1,1001):
    f *= n
    s = s + 1/f

e = s
t = time.time()

print(e)
print("Time Interval:",t-o,"second")