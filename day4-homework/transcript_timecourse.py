#!/usr/bin/env python

"""
Usage: ./timecourse.py <samples.csv> <ctab.dir> <replicates.csv> <gene_name>

- Plot timecourse of FBtr0331261 for females
- Plot timecourse of FBtr0331261 for males
- Plot timecourse of FBtr0331261 for replicates
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gene_name = sys.argv[4]

df_samples = pd.read_csv( sys.argv[1] )
df_rep_samples = pd.read_csv ( sys.argv[3] )
soi_fem = df_samples["sex"] == "female"
soi_male = df_samples["sex"] == "male"
soi_rep_fem = df_rep_samples["sex"] == "female"
soi_rep_male = df_rep_samples["sex"] == "male"

fpkms_fem = []
fpkms_male = []
fpkms_rep_fem = []
fpkms_rep_male = []
fpkms_stdev_fem = []
fpkms_stdev_male = []
fpkms_stdev_rep_fem = []
fpkms_stdev_rep_male = []

for sample in df_samples["sample"][soi_fem]: # Sample contains SRR... names from the samples.csv file
    # Build complete file path
    fname =  os.path.join(sys.argv[2], sample, "t_data.ctab") # passes in the directory, then locates our file; os.path.join joins these three strings with the filepath delimiter this operating system expects
    # Read current sample
    df = pd.read_csv( fname, sep = "\t" )
    # Subset just gene_name rows
    roi = df["gene_name"] == gene_name
    # average the FPKM values across transcripts
    values = df[roi]["FPKM"].values
    average_fpkms = values.sum()/len(values)
    stdev_fpkms = np.std(values)
    # Save FPKM values to list
    fpkms_fem.append(average_fpkms)
    fpkms_stdev_fem.append(stdev_fpkms)
    
for sample in df_samples["sample"][soi_male]: # Sample contains SRR... names from the samples.csv file
    # Build complete file path
    fname =  os.path.join(sys.argv[2], sample, "t_data.ctab") # passes in the directory, then locates our file; os.path.join joins these three strings with the filepath delimiter this operating system expects
    # Read current sample
    df = pd.read_csv( fname, sep = "\t" )
    # Subset just gene_name rows
    roi = df["gene_name"] == gene_name
    # average the FPKM values across transcripts
    values = df[roi]["FPKM"].values
    average_fpkms = values.sum()/len(values)
    stdev_fpkms = np.std(values)
    # Save FPKM values to list
    fpkms_male.append(average_fpkms)
    fpkms_stdev_male.append(stdev_fpkms)
    
for sample in df_rep_samples["sample"][soi_rep_fem]: # Sample contains SRR... names from the samples.csv file
    # Build complete file path
    fname =  os.path.join(sys.argv[2], sample, "t_data.ctab") # passes in the directory, then locates our file; os.path.join joins these three strings with the filepath delimiter this operating system expects
    # Read current sample
    df = pd.read_csv( fname, sep = "\t" )
    # Subset just gene_name rows
    roi = df["gene_name"] == gene_name
    # average the FPKM values across transcripts
    values = df[roi]["FPKM"].values
    average_fpkms = values.sum()/len(values)
    stdev_fpkms = np.std(values)
    # Save FPKM values to list
    fpkms_rep_fem.append(average_fpkms)
    fpkms_stdev_rep_fem.append(stdev_fpkms)
    
for sample in df_rep_samples["sample"][soi_rep_male]: # Sample contains SRR... names from the samples.csv file
    # Build complete file path
    fname =  os.path.join(sys.argv[2], sample, "t_data.ctab") # passes in the directory, then locates our file; os.path.join joins these three strings with the filepath delimiter this operating system expects
    # Read current sample
    df = pd.read_csv( fname, sep = "\t" )
    # Subset just gene_name rows
    roi = df["gene_name"] == gene_name
    # average the FPKM values across transcripts
    values = df[roi]["FPKM"].values
    average_fpkms = values.sum()/len(values)
    stdev_fpkms = np.std(values)
    # Save FPKM values to list
    fpkms_rep_male.append(average_fpkms)
    fpkms_stdev_rep_male.append(stdev_fpkms)
    
print len(fpkms_fem)
print fpkms_male
print fpkms_rep_fem
print fpkms_rep_male
print len(fpkms_stdev_fem)
print fpkms_stdev_male
print fpkms_stdev_rep_fem
print fpkms_stdev_rep_male

plt.figure()
plt.errorbar([0,1,2,3,4,5,6,7], fpkms_fem, yerr = fpkms_stdev_fem, label = "females", c = "red")
plt.errorbar([0,1,2,3,4,5,6,7], fpkms_male, yerr = fpkms_stdev_male, label = "males", c = "blue")
plt.errorbar([4,5,6,7],fpkms_rep_fem, yerr = fpkms_stdev_rep_fem, label = "female replicates", marker = "o", c = "red", ls = "None")
plt.errorbar([4,5,6,7],fpkms_rep_male, yerr = fpkms_stdev_rep_male, label = "male replicates", marker = "o", c = "blue", ls = "None")
plt.legend(loc = 2)
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (FPKM)")
plt.title(gene_name)
plt.xticks([0,1,2,3,4,5,6,7],["10","11","12","13","14A","14B","14C","14D"])
plt.savefig( "transcript_timecourse.png" )
plt.close()