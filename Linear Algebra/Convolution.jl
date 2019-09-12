#### Convolution

"""
Find the coefficients of this polynomial:
p(x) = (1 + x)(2 - x + x^2)(1 + x - 2x^2) = 2 + 3x - 3x^2 - x^3 + x^4 -2x^5
"""

using DSP 

a = [1, 1]                  # coefficients of 1 + x
b = [2,-1, 1]               # coefficients of 2 - x + x^2
c = [1, 1,-2]               # coefficients of 1 + x - 2x^2
d = conv(conv(a,b),c)       # coefficients of product

println(d)                  # [2, 3, -3, -1, 1, -2]

# Construct the Toeploitz Matrix

function toeploitz(b,n)
    m = length(b)
    T = zeros(n+m-1,n)
    for i = 1:m
        T[i:n+m:end] .= b[i]
    end
    return T    
end

a = [-2, 3,-1, 1]
b = [-1, 2, 3]

Tb = toeploitz(b,length(a))
println(Tb)
    # [-1.0  0.0  0.0  0.0; 
    #   2.0 -1.0  0.0  0.0; 
    #   3.0  2.0 -1.0  0.0; 
    #   0.0  3.0  2.0 -1.0; 
    #   0.0  0.0  3.0  2.0; 
    #   0.0  0.0  0.0  3.0]

# 3.1415926535897932384626433832795028841971693993751058

