#!/usr/bin/env python

import sys

fh = sys.stdin
perfect_match = "NH:i:1"

numlines = 0
for line in fh:
    # Don't include any header lines
    if line.startswith("@"):
        continue
    else:
        if perfect_match in line:
            numlines+=1

print "There are %s alignments that map to only one place in the genome." % (str(numlines))