#!/usr/bin/env python

import sys

totallen = 0.0
numlines = 0
for line in sys.stdin:
    line = line.rstrip()
    totallen += float(line)
    numlines += 1

averagelen = float(totallen/numlines)
print "total length: %d, number of lines: %d, average length: %f" % (totallen, numlines, averagelen)