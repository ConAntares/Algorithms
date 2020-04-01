#### Examples of Functions that are not Linear

"""
The componentwise absolute value and the sort function are examples of nonlinear funciton.
These functions are easily computed by `abs` and `sort`. By default, the `sort` function sorts in increasing order,
but this can be changed by adding an optional keyword argument.
"""

using LinearAlgebra

f(x) = abs.(x)              # Componentwise Absolute value
x = [1, 0]
y = [0, 1]
α = -1
β =  2

ra = f(α*x + β*y)
println(ra)                 # [ 1,  2]

rb = α*f(x) + β*f(y)
println(rb)                 # [-1,  2]

g(x) = sort(x, rev=true)    # Sort in Decreasing order

rc = g(α*x + β*y)
println(rc)                 # [ 2, -1]

rd = α*g(x) + β*g(y)
println(rd)                 # [ 1,  0]

