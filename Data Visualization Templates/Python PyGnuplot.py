#### PyGnuplot

import numpy as np
import PyGnuplot as pgl

x = [1,2]
y = np.sin(4*x)
yc = np.sin(4*x)

# pgl.s([x,y], filename='example.pdf')

pgl.s([x,y])
pgl.c("set sample 512")
pgl.c("set title 'Example' font 'CMU-Serif,12'")
pgl.c("set xrange[-2*pi:2*pi]")
pgl.c("plot sin(4*x)")

pgl.c("pause (-1)")