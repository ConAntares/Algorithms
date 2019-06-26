### Running Sum Matrix

# About Running Sum Matrix
"""
R = [ 1 0 0 0;
      1 1 0 0;
      1 1 1 0;
      1 1 1 1 ]
X = [ a b c d ]
R*X = [ a a+b a+b+c a+b+c+d]
"""

using LinearAlgebra

running_sum(n) = LowerTriangular(ones(n,n))

re = running_sum(4)
println(re)
    # [1.0 0.0 0.0 0.0; 
    #  1.0 1.0 0.0 0.0; 
    #  1.0 1.0 1.0 0.0; 
    #  1.0 1.0 1.0 1.0]

re = running_sum(4)*[-1, 1, 2, 0]
println(re)
    # [-1.0, 0.0, 2.0, 2.0]