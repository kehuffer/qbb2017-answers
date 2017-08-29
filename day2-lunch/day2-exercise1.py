#!/usr/bin/env python

import sys

fh = sys.stdin

# Find the number of alignment lines in the file.
numlines = 0
for line in fh:
    # Don't include any header lines
    if line.startswith("@"):
        continue
    else:
        numlines+=1

print "There are %s alignments" % (str(numlines))