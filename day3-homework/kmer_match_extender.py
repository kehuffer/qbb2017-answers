#!/usr/bin/env python

"""
Finds matching kmers between a query sequence and a database of targets.
Extends the matching kmers to find the longest exact match.

usage: ./kmer_match_extender.py <target.fa> <query.fa> <k>
output: target_sequence_name target_sequence_matches_descending_length
"""

import sys
import fasta

target = open(sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3]) # kmer length

target_sequences = {}
query_sequence = ""
target_kmers = {}
query_kmers = {}

# target
for ident, sequence in fasta.FASTAReader(target):
    sequence = sequence.upper()
    target_sequences[ident] = sequence
    for i in range( 0, len(sequence) - k ):
        kmer = sequence[i:i+k]
        if kmer not in target_kmers:
            target_kmers[kmer] = [(ident,i)]
        else:
            target_kmers[kmer].append((ident,i))
            
# query
for ident, sequence in fasta.FASTAReader(query):
    sequence = sequence.upper()
    query_sequence = sequence
    for i in range( 0, len(sequence) - k ):
        kmer = sequence[i:i+k]
        if kmer not in query_kmers:
            query_kmers[kmer] = [i]
        else:
            query_kmers[kmer].append(i)
            
ext_kmer_dict = {}   
         
for kmer in query_kmers:
    if kmer in target_kmers:
        for tk in range(len(target_kmers[kmer])):
            for qk in range(len(query_kmers[kmer])):
                prec = 1
                foll = 0
                extkmer = kmer
                while True: # check whether preceding sequences match
                    target_kmer_ident = target_kmers[kmer][tk][0]
                    target_kmer_pos = target_kmers[kmer][tk][1]
                    query_kmer_pos = query_kmers[kmer][qk]
                    if target_sequences[target_kmer_ident][target_kmer_pos-prec] == query_sequence[query_kmer_pos-prec] and ((target_kmer_pos - prec) >= 0) and ((query_kmer_pos - prec) >= 0):# if the letter in the target sequence at the target position minus n matches the letter in the query sequence at the query position minus n, add it to the kmer and continue
                        extkmer = query_sequence[query_kmer_pos-prec]+extkmer
                        prec += 1
                    else:
                        while True: # check whether following sequences match
                            #print extkmer, target_kmer_ident, (target_kmer_pos+k+foll), len(target_sequences[target_kmer_ident]), (query_kmer_pos+k+foll), len(query_sequence)
                            if target_sequences[target_kmer_ident][target_kmer_pos+k+foll] == query_sequence[query_kmer_pos+k+foll] and ((target_kmer_pos + k + foll) < (len(target_sequences[target_kmer_ident]))) and ((query_kmer_pos + k + foll) < (len(query_sequence))):# if the letter in the target sequence at the target position minus n matches the letter in the query sequence at the query position minus n, add it to the kmer and continue
                                extkmer = extkmer+query_sequence[query_kmer_pos+k+foll]
                                foll += 1
                            else:
                                if target_kmer_ident not in ext_kmer_dict:
                                    ext_kmer_dict[target_kmer_ident] = [extkmer]
                                elif extkmer not in ext_kmer_dict[target_kmer_ident]:
                                    ext_kmer_dict[target_kmer_ident].append(extkmer)
                                #print ext_kmer_dict
                                break
                            break
                        break

for ident, extkmer in ext_kmer_dict.iteritems():
    print ident, sorted(extkmer, key = len)