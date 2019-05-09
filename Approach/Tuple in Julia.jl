#### Tuple

re = (1,2,3,4)
println(re)
    # (1, 2, 3, 4)
println(typeof(re))
    # NTuple{4,Int64}

re = ("a","b","c","d")
println(re)
    # ("a", "b", "c", "d")
println(typeof(re))
    # NTuple{4,String}

re = Tuple([1,2,3,4])
println(re)
    # (1, 2, 3, 4)