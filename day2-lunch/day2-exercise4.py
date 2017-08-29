#!/usr/bin/env python

import sys

fh = sys.stdin
numlines = 0

for line in fh:
    # Don't include any header lines
    if line.startswith("@"):
        continue
    else:
        if numlines < 10:
            print line.split("\t")[2]
            numlines += 1

