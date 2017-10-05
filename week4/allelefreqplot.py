#!/usr/bin/env python

"""
./allelefreqplot.py <plink.frq> <filename>
"""

import sys
import matplotlib.pyplot as plt
import pandas as pd

frq = pd.read_csv(open(sys.argv[1]), delim_whitespace = True)

plt.figure()
plt.hist(frq["MAF"], bins=50)
plt.xlabel("Allele Frequency")
plt.ylabel("Number")
plt.title("Allele Frequency Spectrum")
plt.savefig(sys.argv[2])
plt.close()