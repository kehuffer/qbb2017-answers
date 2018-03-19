#!/usr/bin/env python

'''
./needlemanwunsch.py [datafile_s] [datafile_t]
'''

# 2 alignments; decide which is s and which is t
# find length of each alignment
# create a matrix with size ixj and initialize with correct values in first row and column
# create traceback matrix with size ixj

# for each square in the matrix
# determine v, h, and d (use HoxD70 scoring matrix)
# determine max of these three and assign it to the value in the score matrix
# traceback matrix is v, h, or d, whichever was max
# dictionaries?

import sys
import fasta
import numpy as np

sfile = open(sys.argv[1])
tfile = open(sys.argv[2])

# HoxD70 matrix of Chiaromonte, Yap, Miller 2002,
#              A     C     G     T
sigma = [ [   91, -114,  -31, -123 ],
          [ -114,  100, -125,  -31 ],
          [  -31, -125,  100, -114 ],
          [ -123,  -31, -114,   91 ] ]

gap = 300
hoxd70 = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

for ident, sequence in fasta.FASTAReader(sfile):
    sequence = sequence.upper()
    s = sequence
    
for ident, sequence in fasta.FASTAReader(tfile):
    sequence = sequence.upper()
    t = sequence

slen = len(s)+1
tlen = len(t)+1

# create empty matrices
score = np.zeros((slen,tlen))
traceback = np.chararray((slen,tlen))
    
# initialize matrices
for i in range(1,slen):
    score[i,0] = score[(i-1),0] - gap
for j in range(1,tlen):
    score[0,j] = score[0,(j-1)] - gap

# insert values into score matrix and traceback matrix
for i in range(1,slen):
    for j in range(1,tlen):
        v = score[(i-1),j] - gap
        h = score[i,(j-1)] - gap
        # check which letter is in each string at that point and index into HoxD70 matrix to check
        x = hoxd70[s[i-1]]
        y = hoxd70[t[j-1]]
        d = score[(i-1),(j-1)] + sigma[x][y]
        options = {'v': v, 'h': h, 'd': d}
        max_value = max(options.values())
        score[i,j] = max_value
        max_keys = filter(lambda x:options[x] == max_value, options.keys())
        traceback[i,j] = np.random.choice(max_keys)

# alignment
salign = ""
talign = ""
m = slen - 1
n = tlen - 1
while m > 0 | n > 0:
        # check whether traceback is h, d, or v, and put the correct value into each string
        # if traceback is h, get value for t from current position; s = -
        # if traceback is v, get value for s from current position; t = -
        # if traceback is d, get value for s from current position; get value for t from current position
        if traceback[m,n] == 'h':
            salign = "-" + salign
            talign = t[n-1] + talign
            n -= 1
        elif traceback[m,n] == 'v':
            salign = s[m-1] + salign
            talign = "-" + talign
            m -= 1
        elif traceback[m,n] == 'd':
            salign = s[m-1] + salign
            talign = t[n-1] + talign
            n -= 1
            m -= 1
        
print salign
print talign