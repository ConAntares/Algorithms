#### Broadcast

## Broadcast broadcast(f::Function, As...)
broadcast(+,[1,2,3],[40,50,60],[100,200,300])
    # 3-element Array{Int64,1}:
    #  141
    #  252
    #  363

broadcast(*,[1,2,3],[10,20,30],[100,100,100])
    # 3-element Array{Int64,1}:
    #  2
    #  4
    #  6

broadcast(*,[1,2,3],2)
    # 3-element Array{Int64,1}:
    #  1000
    #  4000
    #  9000

broadcast(x->x^2, [1,2,3])
    # 3-element Array{Int64,1}:
    #  1
    #  4
    #  9

broadcast(tuple, (1//(i+j) for i=1:2, j=1:2))
    # 2×2 Array{Tuple{Rational{Int64}},2}:
    #  (1//2,)  (1//3,)
    #  (1//3,)  (1//4,)

broadcast(tuple, (1//(i+j) for i=1:2, j=1:2), [1 3; 2 4])
    # 2×2 Array{Tuple{Rational{Int64},Int64},2}:
    #  (1//2, 1)  (1//3, 3)
    #  (1//3, 2)  (1//4, 4)