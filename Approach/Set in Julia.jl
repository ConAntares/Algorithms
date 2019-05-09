#### Set

re = Set([1, 2, 3, 4, 5, 1, 3, 5])
println(re)
    # Set([4, 2, 3, 5, 1])

re = Set((1, 2, 3, 4, 5, 2, 4))
println(re)
    # Set([4, 2, 3, 5, 1])

A = Set([1,2,3,4])
B = Set([1,3,5,7])

re = intersect(A,B)
println(re)
    # Set([3, 1])
re = union(A,B)
println(re)
    # Set([7, 4, 2, 3, 5, 1])
