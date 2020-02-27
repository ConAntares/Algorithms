#### Richardson Extrapolation

using DelimitedFiles
using LinearAlgebra
# using Plots; pyplot()

"""
Sn = 1 + 1/2^2 + 1/3^2 + 1/4^2 + ... + 1/n^2
lim(n->∞)Sn = π^2/6 ≈ 1.6449340668482264

R1(n) = ((n+1)*S(n+1)-n*S(n))/factorial(1)
R2(n) = ((n+2)^2*S(n+1)-2*(n+1)^2*S(n+1)+n^2*S(n))/factorial(2)
……
"""

to = time()

A = readdlm("Data/Td.dat")
X = view(A,:,1)
Y = view(A,:,2)

count = length(X)

function RE1(Y)
    R1 = ones(count)
    for i in range(1; stop=count)
        if i in 1:count - 1
            R1[i] = ((i+1)*Y[i+1]-i*Y[i])/factorial(1)
        else
            R1[i] = 0
        end
        i = i + 1
    end
    return R1
end

function RE2(Y)
    R2 = ones(count)
    for i in range(1; stop=count)
        if i in 1:count - 2
            R2[i] = ((i+2)^2*Y[i+2]-2*(i+1)^2*Y[i+1]+i^2*Y[i])/factorial(2)
        else
            R2[i] = 0
        end
        i = i + 1
    end
    return R2
end

U1 = RE1(Y)
U2 = RE2(Y)

td = time() - to
println("The time interval is $td s.")

# plot(fontfamily=("Serif"),dpi=512)
# scatter!(X,Y, color="#B4B4B4",marker=(:circle,10,Plots.stroke(:white)),label="Source")
# plot!(X[1:count-1],U1[1:count-1],color="#FF1E14",label="Foreast")
# plot!(X[1:count-2],U2[1:count-2],color="#1978F0",label="Foreast")