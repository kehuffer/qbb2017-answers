#!/usr/bin/env python

import sys

fh = sys.stdin
numlines = 0
chromosome = "2L"
start = 10000
stop = 20000

for line in fh:
    # Don't include any header lines
    if line.startswith("@"):
        continue
    else:
        if (line.split("\t")[2] == chromosome):
            if ((line.split("\t")[3] >= start) and ((line.split("\t")[3] <= stop))):
                numlines += 1
        
print "There are %s reads on chromosome 2L between positions 10000 and 20000, inclusive." % (str(numlines))

