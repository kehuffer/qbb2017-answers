#!/usr/bin/env python

import sys

fh = sys.stdin

for line in fh:
    # skip header
    if line.startswith ("t_id"):
        continue
    # start and end are in columns 3 and 4
    # extract columns
    fields = line.split("\t")
    # convert to integers
    # subtract
    print int(fields[4]) - int(fields[3])