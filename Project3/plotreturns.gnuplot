plot "avgret.dat" using 1:2 ti ""
set title "Average return obtained by Sarsa after n-th episode"
set xlabel "Episode number (n)"
set ylabel "Average return"
set yrange [-300:-150]
set xrange [-20:10000]
set terminal postscript eps enhanced color
set output "avgret.eps"
replot
