#### Symbol

re = Symbol(:a,:(=),:1,:*,:2,:+,:3)
println(re)
    # a=1*2+3
println(typeof(re))
    # Symbol

re = :[10,20,30]
println(re)
    # [10, 20, 30]

re = :(10,20,30)
println(re) 
    # (10, 20, 30)

re = :(Set(1,2,3,4))
println(re)
    # Set(1, 2, 3, 4)

re = :foo
println(re)
    # foo

re = :[]
println(re)
    # []

re = :()
    # (())