#### Map

## Map map(f::Function, c...) -> collection
map(round,[1.2,2.3,3.4,4.5,5.6])
    # 5-element Array{Float64,1}:
    #  1.0
    #  2.0
    #  3.0
    #  4.0
    #  6.0

map(+,[1,2,3],[40,50,60],[100,200,300])
    # 3-element Array{Int64,1}:
    #  141
    #  252
    #  363

map(*,[1,2,3],[10,20,30],[100,100,100])
    # 3-element Array{Int64,1}:
    #  1000
    #  4000
    #  9000

map(x->x^2,[1,2,3])
    # 3-element Array{Int64,1}:
    #  1
    #  4
    #  9

map(tuple,(1//(i+j) for i=1:2, j=1:2))
    # 2×2 Array{Tuple{Rational{Int64}},2}:
    #  (1//2,)  (1//3,)
    #  (1//3,)  (1//4,)

map(tuple,(1//(i+j) for i=1:2, j=1:2),[1 3; 2 4])
    # 2×2 Array{Tuple{Rational{Int64},Int64},2}:
    #  (1//2, 1)  (1//3, 3)
    #  (1//3, 2)  (1//4, 4)