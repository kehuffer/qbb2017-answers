#!/usr/bin/env python

"""
Finds matching kmers between a query sequence and a database of targets

usage: ./kmer_matcher.py <target.fa> <query.fa> <k>
output: target_sequence_name target_start query_start k_mer
"""

import sys
import fasta

target = open(sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3]) # kmer length

target_kmers = {}
query_kmers = {}

# target
for ident, sequence in fasta.FASTAReader(target):
    sequence = sequence.upper()
    for i in range( 0, len(sequence) - k ):
        kmer = sequence[i:i+k]
        if kmer not in target_kmers:
            target_kmers[kmer] = [(ident,i)]
        else:
            target_kmers[kmer].append((ident,i))
            
# query
for ident, sequence in fasta.FASTAReader(query):
    sequence = sequence.upper()
    for i in range( 0, len(sequence) - k ):
        kmer = sequence[i:i+k]
        if kmer not in query_kmers:
            query_kmers[kmer] = [i]
        else:
            query_kmers[kmer].append(i)

i = 0            
for kmer in query_kmers:
    if kmer in target_kmers:
        for t in range(len(target_kmers[kmer])):
            for q in range(len(query_kmers[kmer])):
                if i < 1000:
                    print target_kmers[kmer][t][0], target_kmers[kmer][t][1], query_kmers[kmer][q], kmer
                    i += 1