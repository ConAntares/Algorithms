#### Julia PyPlot Template 2D

using PyPlot
using PyCall

PyPlot.rc("text", usetex = "true")
PyPlot.rc("font", family = "CMU Serif")

fig = figure(figsize=(8,6))
# fig.suptitle("SupTitle",size=20)
title(raw"Title $\alpha$",size=24)

X = range(-2pi, stop=2pi, length=100)
Y = 1.5 .* sin.(0.3 .+ 0.7X)

plot(X,Y,lw=4, label = raw"Function $f=f(x)$")
legend(loc="best")
grid(true, linestyle="--", color="#D0D0D0", lw=1, alpha=0.5)
tick_params(direction="in", top=true, right=true, bottom=true, left=true, which="both")