set terminal epslatex size 16.5cm, 12cm
set output "daily.tex"
set xrange [0:92]
set yrange [0:10]
set key off
set grid ytics lt 1 lw 4 lc rgb "#bbbbbb"
set grid xtics lt 1 lw 4 lc rgb "#bbbbbb"
set grid mxtics lt 1 lw 2 lc rgb "#dddddd"
set grid mytics lt 1 lw 2 lc rgb "#dddddd"
set title ""
set xlabel "day of quarter"
set xtics 0,5,92
set ytics 0,1,10
set mxtics 2
set mytics 2

set ytics offset -1,0,0

plot "minusone.dat"

