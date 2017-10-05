#!/usr/bin/env python

"""
./pcaplot.py <eigenvec> <filename>
"""

import sys
import matplotlib.pyplot as plt
import pandas as pd

eigenvec = pd.read_csv(open(sys.argv[1]), delimiter = "\t", header = None)

plt.figure()
plt.scatter(eigenvec[2], eigenvec[3])
plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.title("Principle Component Analysis")
plt.savefig(sys.argv[2])
plt.close()