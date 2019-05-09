#### Fibonacci Sequence with Recursion

"""
f(n) =  1                   (n = 1)
        1                   (n = 2)
        f(n-1) + f(n-2)     (n > 2)
"""

import time

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