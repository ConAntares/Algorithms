#### Array in Julia

using LinearAlgebra

## Range Vector
range(1;stop=10)            # 1:10

range(1.0;stop=10.0)        # 1.0:1.0:10.0

range(1;stop=10,step=2)     # 1:2:9

range(1;stop=10,length=5)   # 1.0:2.25:10.0


## Array
# Input a n*m array as the matrix you want to analysis:
A = 
[
    4 2 3 5;
    3 4 6 2;
    5 3 1 4;
]

# Type of elements in array:
eltype(A)       # Int64

# number of elements in array:
length(A)       # 12

# Dimensions of elements in array:
ndims(A)        # 2

# Size of array:
size(A)         # (3, 4)

# Size of array in dimension 1:
size(A,1)       # 3

# Size of array in dimension 2:
size(A,2)       # 4

# The initial array:
Array{Float64}(undef,2,3)
    # 2×3 Array{Float64,2}:
    #  0.0  0.0  0.0
    #  0.0  0.0  0.0

## Special Arrays:
zeros(Float64,2,3)
    # 2×3 Array{Float64,2}:
    #  0.0  0.0  0.0
    #  0.0  0.0  0.0

ones(Float64,2,3)
    # 2×3 Array{Float64,2}:
    #  0.0  0.0  0.0
    #  0.0  0.0  0.0

trues(1,3)
    # 1×3 BitArray{2}:
    #  true  true  true

falses(1,3)
    # 1×3 BitArray{2}:
    #  false  false  false

rand(Float64,1,10)
    # 1×10 Array{Float64,2}:
    #  0.0286736  0.0278282  0.600129  0.0511987  0.280486  0.340728  0.718723  0.810578  0.921655  0.169002

randn(Float64,1,10)
    # 1×10 Array{Float64,2}:
    #  -2.16349  -0.775367  0.597722  -2.65464  -1.4538  1.10059  -0.591062  0.943115  0.220957  -0.327613

Array(UniformScaling{Float64}(1),3,3)
    # 3×3 Array{Float64,2}:
    #  1.0  0.0  0.0
    #  0.0  1.0  0.0
    #  0.0  0.0  1.0

Array(UniformScaling{Float64}(4),3,3)
    # 3×3 Array{Float64,2}:
    #  4.0  0.0  0.0
    #  0.0  4.0  0.0
    #  0.0  0.0  4.0

A = 
[
    1.0 2.0;
    3.0 4.0
]
B =
[
    0.1 0.2;
    0.3 0.4
]

A,B
    # ([1.0 2.0; 3.0 4.0], [0.1 0.2; 0.3 0.4])

(A,B)
    # ([1.0 2.0; 3.0 4.0], [0.1 0.2; 0.3 0.4])

[A,B]
    # 2-element Array{Array{Float64,2},1}:
    #  [1.0 2.0; 3.0 4.0]
    #  [0.1 0.2; 0.3 0.4]

[A B]
    # 2×4 Array{Float64,2}:
    #  1.0  2.0  0.1  0.2
    #  3.0  4.0  0.3  0.4

[A;B]
    # 4×2 Array{Float64,2}:
    #  1.0  2.0
    #  3.0  4.0
    #  0.1  0.2
    #  0.3  0.4

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

broadcast(x->x^2,[1,2,3])
    # 3-element Array{Int64,1}:
    #  1
    #  4
    #  9

broadcast(tuple,(1//(i+j) for i=1:2, j=1:2))
    # 2×2 Array{Tuple{Rational{Int64}},2}:
    #  (1//2,)  (1//3,)
    #  (1//3,)  (1//4,)

broadcast(tuple,(1//(i+j) for i=1:2, j=1:2),[1 3; 2 4])
    # 2×2 Array{Tuple{Rational{Int64},Int64},2}:
    #  (1//2, 1)  (1//3, 3)
    #  (1//3, 2)  (1//4, 4)
    
## Point Operation
foo = x -> x^3
foo.(A)
    # 2×2 Array{Float64,2}:
    #   1.0   8.0
    #  27.0  64.0

Tuple(A)
    # (1.0, 3.0, 2.0, 4.0)

Set(A)
    # Set([4.0, 2.0, 3.0, 1.0])

A.^2
    # 2×2 Array{Float64,2}:
    #  1.0   4.0
    #  9.0  16.0

## Sort Operation
sort([-1,-2,0,2,1],rev=true)
    # 5-element Array{Int64,1}:
    #   2
    #   1
    #   0
    #  -1
    #  -2

sort([-1,-2,0,2,1],rev=false)
    # 5-element Array{Int64,1}:
    #  -2
    #  -1
    #   0
    #   1
    #   2

sort([-1,-2,0,2,1],by=abs,rev=false)
    # 5-element Array{Int64,1}:
    #   0
    #  -1
    #   1
    #  -2
    #   2

sort([3 1 5; 2 10 7; 3 2 9],dims=1,alg=MergeSort)
    # 3×3 Array{Int64,2}:
    #  2   1  5
    #  3   2  7
    #  3  10  9

# ## More Information
# """
# Please see the Julia documentation for more information:
# https://docs.julialang.org/en/latest/
# """