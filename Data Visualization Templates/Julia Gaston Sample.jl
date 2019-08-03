#### Julia Gaston Sample

#plotcom = "set terminal cairolatex standalone; set output '$figurename.tex'"

using Gaston

X = range(-2pi, stop=2pi, length=100)
Y = 1.5 .* sin.(0.3 .+ 0.7X)

plotcom = ""
figurename = "JuliaGnuplot"

plot(X, Y, font="Serif,16", plotstyle="lines", title="Title" ,legend="Function", gpcom=plotcom)