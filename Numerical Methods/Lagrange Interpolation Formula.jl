#### Lagrange Interpolation Formula

using DelimitedFiles
using Plots

A = readdlm("Numerical Methods/Data/data02.dat")
X = view(A,:,1)
Y = view(A,:,2)

plot