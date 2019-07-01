#### 2D Plot with Gnuplot Lines

set termoption enhanced

set title   "Title" font "CMU-Serif"
set xlabel  "X-Label" font "CMU-Serif"
set ylabel  "Y-Label" font "CMU-Serif"
set xrange  [-0.1: 4.1]
set yrange  [-0.1: 2.1]
set xtics   0.0,0.5,4.0 font "CMU-Serif"
set ytics   0.0,0.5,4.0 font "CMU-Serif"
set key     font "CMU-Serif"

plot    "../Data/data00.dat"    using 1:2 with lines linecolor "#F0140A" linewidth 2 title "Function 1",\

set output
pause (-1)