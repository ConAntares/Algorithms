#### Julia Gnuplot Sample

using Gnuplot

X = range(-2pi, stop=2pi, length=100)
Y = 1.5 .* sin.(0.3 .+ 0.7X)

@gp(
    title = "My title",
    xrange = (-7,7),    yrange = (-4,4),
    xlabel = "X label", ylabel = "Y label", 
    # "set output",
    X, Y, "with lines",
    save(term="cairolatex standalone", output="JuliaGnuplot.tex")
);

# @gp tit="My title" xr=(-7,7) yr=(-4,4) xlab="X label" ylab="Y label" X Y "w l"
# save(term="cairolatex standalone", output="JuliaGnuplot.tex")