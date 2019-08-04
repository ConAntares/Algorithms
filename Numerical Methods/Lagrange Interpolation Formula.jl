#### Lagrange Interpolation Formula

using DelimitedFiles
using Plots; pyplot()

to = time()

function lagrange_interpolate(X,Y,t)
    C = ones(length(X))
    d = 0.0
    for i = 1:length(X)
        for j = [1:i-1;i+1:length(X)]
            C[i] = C[i]*(t-X[j])/(X[i]-X[j])
        end
        d = d + Y[i]*C[i]
    end
    return d
end

function lagrange_interpolate_plus(X,Y,t)
    idxs = eachindex(X)
    sum(Y[i] * prod((t-X[j])/(X[i]-X[j]) for j in idxs if j != i) for i in idxs)
end

A = readdlm("Data/dataSim.dat")
X = view(A,:,1)
Y = view(A,:,2)
T = 1.0:0.1:2.0
U = [lagrange_interpolate_plus(X, Y, t) for t in T]

td = time() - to
println("The time interval is $td s.")

plot(fontfamily=("Serif"),dpi=512)
# scatter!(X,Y,color="#32B432",marker=(:circle,10,Plots.stroke(:white)),label="Source")
# scatter!(T,U,color="#00B4DC",marker=(:cross,10,Plots.stroke(:white)),label="Foreast")
plot!(X,Y,color="#32B432",marker=(:circle,10,Plots.stroke(:white)),label="Source")
plot!(T,U,color="#00B4DC",marker=(:cross,10,Plots.stroke(:white)),label="Foreast")

savefig("U.pdf")