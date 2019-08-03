set term tikz standalone size 800, 600

set ylabel "{\LaTeX\ -- $ \gamma $}"
set xlabel "{\LaTeX\ -- $ x $}"

set output "example.tex"
plot [0:1] gamma(x) title "$ \gamma(x) $"
set output
!pdflatex example