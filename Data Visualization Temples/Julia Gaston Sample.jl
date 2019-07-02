#### Julia Gaston Sample

using Gaston

t = -4:0.01:4

figurename = "JuliaGnuplot"
postcomm = "set terminal cairolatex standalone; set output '$figurename.tex'"
plot(t, sinc.(t), font="Cambria,12", plotstyle="lines", legend="Function", gpcom=postcomm)