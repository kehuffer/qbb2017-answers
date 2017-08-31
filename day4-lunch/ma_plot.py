#!/usr/bin/env python

"""
Usage: ./ma_plot.py <x_plot> <y_plot> <prefix>
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x_df = pd.read_csv( sys.argv[1], sep = "\t" )
y_df = pd.read_csv( sys.argv[2], sep = "\t" )

x_log2 = np.log2(x_df["FPKM"]+1)
y_log2 = np.log2(y_df["FPKM"]+1)

m = x_log2 - y_log2
a = 0.5*(x_log2 + y_log2)
print m
print a

# M = log2(R)-log2(G)
# A = 0.5 (log2(R) + log2(G))

plt.figure()
plt.scatter(a,m,alpha = 0.5)

plt.title("MA Plot of FPKM values of SRR072893 and SRR072915")

plt.xlabel("A")
plt.ylabel("M")
plt.savefig(sys.argv[3] + ".png")
plt.close()

