#### Elementary Matrix

A = 
[
    4 2 3 5;
    3 4 6 2;
    5 3 1 4;
]

println(eltype(A))      # Int64
println(length(A))      # 12
println(ndims(A))       # 2
println(size(A))        # (3,4)
println(size(A,1))      # 3
println(size(A,2))      # 4