#### Dict

re = Dict(1=>1.1, 2=>2.2, 3=>3.3)
println(re)
    # Dict(2=>2.2,3=>3.3,1=>1.1)
println(typeof(re))
    # Dict{Int64,Float64}

re = Dict(i=>i^2 for i in 1:4)
println(re)
    # Dict(4=>16,2=>4,3=>9,1=>1)