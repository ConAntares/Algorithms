#### Factorial

import math
import numpy as np
import sys
import time

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