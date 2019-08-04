#### 2D Plotting with Plots.jl in Julia

## With PyPlot backend

using Plots; pyplot()
using LaTeXStrings

Plots.PyPlot.rc("text", usetex = "true")
Plots.PyPlot.rc("font", family = "CMU Serif")

X = range(-4pi, 4pi, length=100)
Y = pi/2 .* sin.(1/2 .+ (pi/4)X)

plot(dpi=256, gridls=:dash, legend=:topright, frame=:both,
     fgborder="#505050",fglegend="#A0A0A0", fgaxis="#505050", tickfontsize=10, legendfontsize=10)
plot!(X,Y, title = L"Title $\alpha$", lw=2, label=L"wave $f=f(x)$", annotation=(1, 1, L"Annotation $\beta$"))

Plots.savefig("Plots.pdf")