#!/usr/bin/env python

"""
./convertpheno.py <phenotypes_file.txt>
"""
import sys

pheno = open(sys.argv[1])

for line in pheno:
    if line.startswith("\t"):
        print "FID\tIID" + line.rstrip("\n\r")
    else:
        split_lines = line.rstrip("\n\r").split("\t")
        list_to_join = split_lines[0].split("_")
        list_to_join = list_to_join + split_lines[1:]
        joined_line = "\t".join(list_to_join)
        print joined_line
