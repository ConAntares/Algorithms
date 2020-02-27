#### Taylor Approximation

# About Taylor Approximation
"""
The first order Taylor Approximation of a function f: R^n → R, at the point z, is the affine function of x given by
fa(x) = f(z) + (∇f(z))'(x-z)
For x near z, fa(x) is very close to f(x).
"""

# A function and its Gradient
f(x)  = x[1] + exp(x[2] - x[1])
∇f(z) = [1 - exp(z[2] - z[1]), exp(z[2] - z[1])]
z = [1, 2]

# The Taylor Approximation
fa(x) = f(z) + (∇f(z))'*(x-z)

re = f([1,2])
println(re)     # 3.718281828459045
re = fa([1,2])
println(re)     # 3.718281828459045