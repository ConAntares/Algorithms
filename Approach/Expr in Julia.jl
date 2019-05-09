#### Expr

re = :(1 + 2)
println(re)
    # 1 + 2
println(typeof(re))
    # Expr
# println(dump(re))
    # head: Symbol call
    # args: Array{Any}((3,))
    #   1: Symbol +
    #   2: Int64 1
    #   3: Int64 2
println(re.head)
    # call
println(re.args)
    # Any[:+, 1, 2]
println(eval(re))
    # 3