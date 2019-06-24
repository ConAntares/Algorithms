#### Harmonic

using LinearAlgebra
using Plots; pyplot()

# Harmonic Series
"""
Sum_(k=1)^(∞)(1/k) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n + ...
"""

function Harmonic(n)
    harmo = 0
    count = 1
    while count <= n
        harmo = harmo + 1/count
        count = count + 1
    end
    return harmo
end

N = 1:1:1000
H = [Harmonic(n) for n in N]

plot(fontfamily=("Serif") ,dpi=1024)
scatter!(N,H,color="#00B4DC", label="Harmonic Series")