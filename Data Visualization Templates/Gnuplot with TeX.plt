set term tikz standalone size 7cm, 3cm fontscale 0.6
set ylabel "{\LaTeX\ -- $ \gamma $}"
set xlabel "{\LaTeX\ -- $ x $}"
set output "example.tex"
plot [0:1] gamma(x) title "$ \gamma(x) $"
set output
!pdflatex example