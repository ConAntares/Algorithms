#### Linear and Affine Equation

using LinearAlgebra

A = [-0.1  2.8 -1.6;
      2.3 -0.6 -3.6]

f(x) = A*x

x = [1, 2, 3]
y = [4, 5, 6]

α =  0.5
β = -1.6

r = f(α*x + β*y)
println(r)          # [-6.05, 19.79]

e = α*f(x) + β*f(y)
println(e)          # [-6.05, 19.79]

n = norm(r-e)
println(n)          # 4.440892098500626e-15

B = [0,1,0]
u = f(B)
println(u)          # [2.8, -0.6]