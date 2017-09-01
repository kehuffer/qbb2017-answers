#!/usr/bin/env python

"""
Perform ordinary linear regression for each of the four marks to determine how predictive each is of gene expression.

usage: ./linear_regression.py <folder>
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import os

column = 5

h3k27me3 = pd.read_csv("H3K27me3.tab", sep="\t", header=None, index_col = 0) # replace number indices with the transcript name from the original file

h3k36me3 = pd.read_csv("H3K36me3.tab", sep="\t", header=None, index_col = 0) # replace number indices with the transcript name from the original file

h3k4me3 = pd.read_csv("H3K4me3.tab", sep="\t", header=None, index_col = 0) # replace number indices with the transcript name from the original file

h3k9me3 = pd.read_csv("H3K9me3.tab", sep="\t", header=None, index_col = 0) # replace number indices with the transcript name from the original file

df_ctab = pd.read_csv( "~/data/results/stringtie/SRR072893/t_data.ctab", sep="\t", index_col = "t_name")

reg = pd.concat( (h3k27me3[column], h3k36me3[column], h3k4me3[column], h3k9me3[column], df_ctab["FPKM"]), 1, join = "inner")

model = sm.OLS(reg["FPKM"], reg.iloc[:,:4])
results = model.fit()
print results.summary()

#FPKM is dependent, independent variable is the coverage