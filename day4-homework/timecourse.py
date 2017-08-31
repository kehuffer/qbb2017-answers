#!/usr/bin/env python

"""
Usage: ./timecourse.py <samples.csv> <ctab.dir> <replicates.csv>

- Plot timecourse of FBtr0331261 for females
- Plot timecourse of FBtr0331261 for males
- Plot timecourse of FBtr0331261 for replicates
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

transcript = "FBtr0331261"

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

for sample in df_samples["sample"][soi_fem]: # Sample contains SRR... names from the samples.csv file
    # Build complete file path
    fname =  os.path.join(sys.argv[2], sample, "t_data.ctab") # passes in the directory, then locates our file; os.path.join joins these three strings with the filepath delimiter this operating system expects
    # Read current sample
    df = pd.read_csv( fname, sep = "\t" )
    # Subset just Sxl rows
    roi_fem = df["t_name"] == transcript
    # Save FPKM values to list
    fpkms_fem.append(df[roi_fem]["FPKM"].values)
    
for sample in df_samples["sample"][soi_male]: # Sample contains SRR... names from the samples.csv file
    # Build complete file path
    fname =  os.path.join(sys.argv[2], sample, "t_data.ctab") # passes in the directory, then locates our file; os.path.join joins these three strings with the filepath delimiter this operating system expects
    # Read current sample
    df = pd.read_csv( fname, sep = "\t" )
    # Subset just Sxl rows
    roi_male = df["t_name"] == transcript
    # Save FPKM values to list
    fpkms_male.append(df[roi_male]["FPKM"].values)
    
for sample in df_rep_samples["sample"][soi_rep_fem]: # Sample contains SRR... names from the samples.csv file
    # Build complete file path
    fname =  os.path.join(sys.argv[2], sample, "t_data.ctab") # passes in the directory, then locates our file; os.path.join joins these three strings with the filepath delimiter this operating system expects
    # Read current sample
    df = pd.read_csv( fname, sep = "\t" )
    # Subset just Sxl rows
    roi_rep_fem = df["t_name"] == transcript
    # Save FPKM values to list
    fpkms_rep_fem.append(df[roi_rep_fem]["FPKM"].values)
    
for sample in df_rep_samples["sample"][soi_rep_male]: # Sample contains SRR... names from the samples.csv file
    # Build complete file path
    fname =  os.path.join(sys.argv[2], sample, "t_data.ctab") # passes in the directory, then locates our file; os.path.join joins these three strings with the filepath delimiter this operating system expects
    # Read current sample
    df = pd.read_csv( fname, sep = "\t" )
    # Subset just Sxl rows
    roi_rep_male = df["t_name"] == transcript
    # Save FPKM values to list
    fpkms_rep_male.append(df[roi_rep_male]["FPKM"].values)
    
print fpkms_fem
print fpkms_male
print fpkms_rep_fem
print fpkms_rep_male

plt.figure()
plt.plot(fpkms_fem,"r", label = "females")
plt.plot(fpkms_male,"b", label = "males")
plt.plot([4,5,6,7],fpkms_rep_fem,"or", label = "female replicates")
plt.plot([4,5,6,7],fpkms_rep_male,"ob", label = "male replicates")
plt.legend(loc = 2)
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (FPKM)")
plt.title("Sxl")
plt.xticks([0,1,2,3,4,5,6,7],["10","11","12","13","14A","14B","14C","14D"])
plt.savefig( "timecourse.png" )
plt.close()