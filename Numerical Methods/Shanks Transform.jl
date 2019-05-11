#### Shanks Transform

using DelimitedFiles
using LinearAlgebra
using Plots; pyplot()

"""
L[i] = (S[i]^2-S[i-1]*S[i+1])/(2*S[i]-S[i-1]-S[i+1])
"""

A = readdlm("Data/Tr.dat")
X = view(A,:,1)
Y = view(A,:,2)

count = length(X)

L1 = ones(count)
for i in range(1; stop = count)
    if i in 2:count-1
        L1[i] = (Y[i]^2-Y[i-1]*Y[i+1])/(2*Y[i]-Y[i-1]-Y[i+1])
    else
        L1[i] = 0
    end
    i = i + 1
end

L2 = ones(count)
for i in range(1; stop = count)
    if i in 2:count-1
        L2[i] = (L1[i]^2-L1[i-1]*L1[i+1])/(2*L1[i]-L1[i-1]-L1[i+1])
    else
        L2[i] = 0
    end
    i = i + 1
end

L3 = ones(count)
for i in range(1; stop = count)
    if i in 2:count-1
        L3[i] = (L2[i]^2-L2[i-1]*L2[i+1])/(2*L2[i]-L2[i-1]-L2[i+1])
    else
        L3[i] = 0
    end
    i = i + 1
end

L4 = ones(count)
for i in range(1; stop = count)
    if i in 2:count-1
        L4[i] = (L3[i]^2-L3[i-1]*L3[i+1])/(2*L3[i]-L3[i-1]-L3[i+1])
    else
        L4[i] = 0
    end
    i = i + 1
end

plot(fontfamily=("Serif"),dpi=512)
scatter!(X,Y, color="#B4B4B4",marker=(:circle,10,Plots.stroke(:white)),label="Source")
plot!(X[2:count-1],L1[2:count-1],color="#F0140A",label="Foreast")
plot!(X[3:count-2],L2[3:count-2],color="#FFC814",label="Foreast")
plot!(X[4:count-3],L3[4:count-3],color="#00A0DC",label="Foreast")
plot!(X[5:count-4],L4[5:count-4],color="#A064DC",label="Foreast")