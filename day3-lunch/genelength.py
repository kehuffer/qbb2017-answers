#!/usr/bin/env python

import sys

totallen = 0.0
numlines = 0
linelist = []
for line in sys.stdin:
    line = line.rstrip()
    totallen += float(line)
    numlines += 1
    linelist.append(int(line))

averagelen = float(totallen/numlines)
maxlen = int(max(linelist))
minlen = int(min(linelist))
print "total length: %d, number of genes: %d, maximum length: %d, minimum length: %d, average length: %f" % (totallen, numlines, maxlen, minlen, averagelen)