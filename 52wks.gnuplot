set terminal epslatex
set output "52wk.tex"
set xrange [0:52]
set yrange [0:10]
set key off
set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set grid mxtics lt 0 lw 0 lc rgb "#dddddd"
set grid mytics lt 0 lw 0 lc rgb "#dddddd"
set title ""
set label 1 ">" at graph 0,1.125 left
set ylabel ">                                                                <"
set xlabel "week of year"
set xtics 0,2,52
set ytics 0,1,10
set mxtics 2
set mytics 2

set ytics offset -1,0,0

plot "minusone.dat"

