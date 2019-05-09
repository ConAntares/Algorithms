#### Elementary Array

A = [0,1,2,3,4,5,6,7,8,9]

println(A)          # [1, 2, 3, 4, 5]
println(A[1])       # 0
println(A[1:5])     # [0, 1, 2, 3, 4]
println(A[5:1])     # int64()
println(typeof(A))  # Array{Int64,1}
println(eltype(A))  # Int64
println(length(A))  # 10
println(ndims(A))   # 1
println(size(A))    # (10,)
println(size(A,1))  # 10
println(size(A,2))  # 1
println(size(A,3))  # 1

B = float(A)
println(B)          # [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

C = float([0,1,2,3])
println(C)          # [0.0, 1.0, 2.0, 3.0]