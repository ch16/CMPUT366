plot "steps.dat" using 1:2 ti ""
set title "Number of steps taken by n-th episode"
set xlabel "Episode number (n)"
set ylabel "Number of steps"
set yrange [50:3000]
set xrange [-400:400]
set terminal postscript eps enhanced color
set output "steps.eps"
replot
