#!/usr/bin/env python
# Documentation
# $ cat <file> | ./day2-homework-1.py > <formatted_output_file>


import sys

targetstr = "DROME"

for line in sys.stdin:
    if targetstr in line:
        # Remove any newlines from end of line,
        # then split using tab as delimiter
        # -> List of strings representing fields
        fields = line.rstrip("\r\n").split()
        if len(fields) == 4:
            flybase = fields[3]
            uniprot = fields[2]
            print flybase, "\t", uniprot
        else:
            continue