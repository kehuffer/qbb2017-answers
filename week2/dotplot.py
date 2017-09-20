#!/usr/bin/env python
"""
./dotplot.py <alignment.txt> <plot filename> <plot title>
Produce a dotplot from LASTZ alignment data
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = sys.argv[1]
plot_filename = sys.argv[2]
plot_title = sys.argv[3]

alignment = pd.read_csv(filename, sep = "\t")
alignment.columns = ['start1','end1','start2','end2','size2']

alignment['contigs_axis'] = alignment['size2'].cumsum(axis=0)
alignment['contig_start'] = alignment['contigs_axis'] - alignment['size2'] + alignment['start2']
alignment['contig_end'] = alignment['contigs_axis'] - alignment['size2'] + alignment['end2']

plt.figure()
plt.plot([alignment.start1, alignment.end1], [alignment.contig_start, alignment.contig_end])
plt.xlabel("Reference Genome (bp)")
plt.ylabel("Contig (bp)")
plt.xlim(0,100000)
plt.suptitle(plot_title)
plt.savefig(plot_filename + ".png")

plt.figure()
plt.plot([alignment.start1, alignment.end1], [alignment.contig_start, alignment.contig_end])
plt.xlabel("Reference Genome (bp)")
plt.ylabel("Contig (bp)")
plt.suptitle(plot_title + "\nWhole Genome")
plt.savefig(plot_filename + "_whole_genome.png")
plt.close()