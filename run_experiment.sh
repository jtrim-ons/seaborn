#!/bin/bash

python3 swarmplot_experiment.py > swarmplot_experiment_results.txt

cat swarmplot_experiment_results.txt | awk '
BEGIN {print "dist,n,classic_width,compact_width,classic_time,compact_time"}
NR % 6 == 1 {a = $1}
NR % 6 == 2 {b = $1}
NR % 6 == 3 {c = $1}
NR % 6 == 4 {d = $1}
NR % 6 == 5 {e = $1}
NR % 6 == 0 {f = $1; print a "," b "," c "," d "," e "," f}
' > swarmplot_experiment_results.csv

python3 scatter.py
