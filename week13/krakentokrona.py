#!/usr/bin/env python

"""
./krakentokrona.py file.kraken
"""

import sys

data = open(sys.argv[1])

kronadict = {}

for line in data:
    items = line.strip('\n').split('\t')
    if items[1] in kronadict:
        kronadict[items[1]] += 1
    else:
        kronadict[items[1]] = 1

for key in kronadict:
    print str(kronadict[key]) + '\t' + '\t'.join(key.split(';'))
    