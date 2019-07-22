#### Julia Gaston Sample

using Gaston; plotcom = ""

X = range(-2pi, stop=2pi, length=100)
Y = 1.5 .* sin.(0.3 .+ 0.7X)

figurename = "JuliaGnuplot"
#plotcom = "set terminal cairolatex standalone; set output '$figurename.tex'"
plot(X, Y, font="Cambria,12", plotstyle="lines", legend="Function", gpcom=plotcom)