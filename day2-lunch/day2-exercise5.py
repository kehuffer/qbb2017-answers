#!/usr/bin/env python

import sys

fh = sys.stdin
MAPQsum = 0
numlines = 0

for line in fh:
    # Don't include any header lines
    if line.startswith("@"):
        continue
    else:
        MAPQsum += int(line.split("\t")[4])
        numlines += 1
        
print "The average MAPQ score is %s." % (str(float(MAPQsum/numlines)))

