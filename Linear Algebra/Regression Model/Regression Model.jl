#### Regression Model

# About Regression Model
"""
Regression Model is the affine function of x given by
    f(x) = x'β + v
where the n-vector β and the scalar v are the parameters in the model.
Regression Model is used to guess or approximate a real or observed value
of the number y that is associated with x.
"""

using LinearAlgebra
using VMLS

# Parameters
β = [148.73, -18.85]
v = 54.40
D = house_sales_data()

yD = D["price"]
X  = [D["area"] D["beds"]]'

ŷ(x)  =  x' * β .+ v    # Vector of predicted outcomes
rd(x) = yD - ŷ(x)       # Vector of predicted errors

# RMS prediction error
println(rms(rd(X)))

# Compare with standard deviation of prices
println(stdev(ŷ(X)))