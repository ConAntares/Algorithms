#### Unit Vectors

using LinearAlgebra

unit_vector(i,n) = [zeros(i-1); 1; zeros(n-i)]

println(unit_vector(2,4))   # [0.0, 1.0, 0.0, 0.0]