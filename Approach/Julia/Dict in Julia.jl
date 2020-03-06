#### Dict

re = Dict(1=>1.1, 2=>2.2, 3=>3.3, 4=>4.4)
println(re)
    # Dict(4=>4.4,2=>2.2,3=>3.3,1=>1.1)
println(typeof(re))
    # Dict{Int64,Float64}
println(length(re))
    # 4
println(re.count)
    # 4 
println(keys(re))
    # [4, 2, 3, 1]
println(values(re))
    # [4.4, 2.2, 3.3, 1.1]
get!(re,5,5.5)
println(re)
    # Dict(4=>4.4,2=>2.2,3=>3.3,5=>5.5,1=>1.1)
rf = collect(values(re))
print(rf)
    # [4.4, 2.2, 3.3, 5.5, 1.1]

re = Dict(i=>i^2 for i in 1:4)
println(re)
    # Dict(4=>16,2=>4,3=>9,1=>1)
println(re[1]," ",re[2]," ",re[3]," ",re[4])
    # 1 4 9 16