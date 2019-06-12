#### Distance

using LinearAlgebra

# About Distance
"""
The distance between two vectors is that:
    dist(A,B) = ‖A-B‖
"""

u = [1.8, 2.0,-3.6, 4.7]
v = [0.6, 2.1, 1.9,-1.4]
w = [2.0, 1.9,-4.0,-3.2]

println(norm(u-v))  # 8.30120473184465
println(norm(v-w))  # 6.328506932918696
println(norm(w-u))  # 7.913279977354524