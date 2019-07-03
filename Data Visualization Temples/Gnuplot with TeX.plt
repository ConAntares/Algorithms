wrap(TeXstring) = '\begin{document} '.TeXstring.' \end{document}'
title = '\TeX\ is Number $\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$'
set print 'eq.tex'
print wrap(title)
unset print
!latex2png eq
!display eq.png