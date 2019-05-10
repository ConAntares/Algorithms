#### Elementary Matrix

A = 
[
    0.0 0.1 0.2 0.3 0.4;
    1.8 1.6 1.4 1.2 1.0;
    2.1 2.3 2.5 2.7 2.9;
]

println(eltype(A))      # Float64
println(length(A))      # 15
println(ndims(A))       # 2
println(size(A))        # (3,5)
println(size(A,1))      # 3
println(size(A,2))      # 5