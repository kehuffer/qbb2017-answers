#!/usr/bin/env python
"""
./contig_stats.py <contigs.fa>
Compute number of contigs, minimum/maximum/average contig length, and N50
"""

import sys
import fasta
import itertools
import numpy as np

contig_file = open(sys.argv[1])

contig_lengths = []
for ident, sequence in fasta.FASTAReader(contig_file):
    contig_lengths.append(len(sequence))
    
number_contigs = len(contig_lengths)
min_contig_length = min(contig_lengths)
max_contig_length = max(contig_lengths)
avg_contig_length = sum(contig_lengths)/len(contig_lengths)

contig_lengths.sort()

i = 0
contig_sum = 0
while contig_sum < sum(contig_lengths)/2:
    contig_sum += contig_lengths[i]
    i += 1
contig_n50 = contig_lengths[i]

print "number of contigs: ", number_contigs
print "minimum contig length: ", min_contig_length
print "maximum contig length: ", max_contig_length
print "average contig length: ", avg_contig_length
print "N50: ", contig_n50