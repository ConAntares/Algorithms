#### Basic Operation of Vector

# Input a 1*n array as the matrix you want to analysis.
A = [1,2,3]
B = [4,6,8]

# Vector Addition:
Va = A+B
    # [5, 8, 11]

# Vector Subtraction:
Vs = A-B
    # [-3, -4, -5]

# Scalar-Vector Multiplication:
Vc = 1.2*A
    # [1.2, 2.4, 3.6]

# Scalar-Vector Division:
Vd = A/1.2
     # [0.833333, 1.66667, 2.5]

# Scalar-Vector addition:
Vr = A.+3.0
    # [4.0, 5.0, 6.0]

# Elements Product:
Vp = A.*B
    # [4, 12, 24]

# Inner Product:
Vi = A'*B
    # 40

# Cross Product:
Vo = A*B'
    # 3×3 Array{Int64,2}:
    #   4   6   8
    #   8  12  16
    #  12  18  24

# Rotation matrix:
α = pi/4
R = 
[
    cos(α) -sin(α);
    sin(α) cos(α)
]
    # 2×2 Array{Float64,2}:
    #  0.707107  -0.707107
    #  0.707107   0.707107
Si = [2 1]
St = Si*R
    # 1×2 Array{Float64,2}:
    #  2.12132  -0.707107