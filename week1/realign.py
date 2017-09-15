#!/usr/bin/env python

"""
realign.py <protein alignment.fa> <all nucleotide homologues.fa>
"""

import sys
import fasta
import itertools
import numpy as np
import matplotlib.pyplot as plt

protein = open(sys.argv[1])
nucleotide = open(sys.argv[2])

prot_seq = []
for ident, sequence in fasta.FASTAReader(protein):
    prot_seq.append(sequence)
    
nuc_seq = []       
for ident, sequence in fasta.FASTAReader(nucleotide):
    nuc_seq.append(sequence)
    
alignment = itertools.izip (prot_seq, nuc_seq)

nuc_codons = []
protein_codons = []
for (protein, nucleotide) in alignment:
    homologue_nuc_codons = []
    homologue_prot_codons = []
    i = 0
    for character in protein:
        homologue_prot_codons.append(character)
        if character == "-":
            homologue_nuc_codons.append("---")
        else:
            homologue_nuc_codons.append(nucleotide[(3*i):((3*i)+3)])
            i += 1
    nuc_codons.append(homologue_nuc_codons)
    protein_codons.append(homologue_prot_codons)

codon_dS = [0] * len(nuc_codons[0])
codon_dN = [0] * len(nuc_codons[0])

j = 0
for j in range(len(nuc_codons)):
    i = 0
    for i in range(len(nuc_codons[j])):
        if nuc_codons[j][i] == nuc_codons[0][i]:
            continue
        elif protein_codons[j][i] == protein_codons[0][i]:
            codon_dS[i] = codon_dS[i] + 1
        else:
            codon_dN[i] = codon_dN[i] + 1

difference = []
ratio = []
log_ratio = []
valid_ratio = []
k = 0
for k in range(len(codon_dS)):
    difference.append(codon_dN[k]-codon_dS[k])
    if codon_dN[k] == 0 or codon_dS[k] == 0:
        ratio.append(None)
        log_ratio.append(None)
    else:
        ratio.append(codon_dN[k]/float(codon_dS[k]))
        log_ratio.append(np.log10(codon_dN[k]/float(codon_dS[k])))
        valid_ratio.append(codon_dN[k]/float(codon_dS[k]))

z_scores = []
custom_color = []
std_difference = np.std(difference)
for diff in difference:
    z = (diff - 0)/std_difference
    z_scores.append(z)
    if z > 1.96:
        custom_color.append("r")
    else:
        custom_color.append("k")

z_scores_ratio = []
custom_color_ratio = []
std_difference_ratio = np.std(valid_ratio)
for rat in ratio:
    if rat != None:
        z = (rat - 1)/std_difference_ratio
        z_scores_ratio.append(z)
    if z > 1.96:
        custom_color_ratio.append("r")
    else:
        custom_color_ratio.append("k")

plt.figure()
plt.scatter(range(len(difference)), difference, c = custom_color)
plt.xlabel("Codon")
plt.ylabel("dN - dS")
plt.suptitle("Difference")
plt.savefig("difference.png")
plt.close()

plt.figure()
plt.scatter(range(len(log_ratio)), log_ratio, c = custom_color_ratio)
plt.xlabel("Codon")
plt.ylabel("log ( dN / dS )")
plt.suptitle("Ratio")
plt.savefig("ratio.png")
plt.close()

