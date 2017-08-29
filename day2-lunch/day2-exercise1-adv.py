#!/usr/bin/env python

import sys

fh = sys.stdin
countrev = 0
countfor = 0

for line in fh:
    # Don't include any header lines
    if line.startswith("@"):
        continue
    else:
        # spliced alignments contain N in CIGAR
        binflag = int(line.split("\t")[1])
        if binflag & 16:
            countrev += 1
        else:
            countfor += 1

print "There are %s forward alignments and %s reverse alignments." % (str(countfor),str(countrev))
        

