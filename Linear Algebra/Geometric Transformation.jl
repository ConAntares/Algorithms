#### Geometric Transformation

rot(θ) = [cos(θ) -sin(θ);
          sin(θ)  cos(θ)]

θ = pi/3

A = [[1,0],[1.5,0],[2,0],[1,0.25],[1.5,0.25],[1,0.5]]
R = [rot(θ)*p for p in A]

Xa = [c[1] for c in A]; Ya = [c[2] for c in A]
Xr = [c[1] for c in R]; Yr = [c[2] for c in R]

R
    # [0.5,         0.866025]
    # [0.75,        1.29904]
    # [1.0,         1.73205]
    # [0.283494,    0.991025]
    # [0.533494,    1.42404]
    # [0.0669873,   1.11603]