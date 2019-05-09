#### Fibonacci Sequence with Iteration

"""
f(n) =  1                   (n = 1)
        1                   (n = 2)
        f(n-1) + f(n-2)     (n > 2)
"""

import time

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
print("Fibonacci with Iteration: The time interval is %f s." %td)