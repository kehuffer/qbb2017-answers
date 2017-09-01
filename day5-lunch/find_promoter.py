#!/usr/bin/env python

"""
Determine an approximation of the promoter region for each of the transcripts present in your SRR072893/t_data.ctab file. Do so by finding the region +/- 500bp from the transcription start site of each transcript. Save as a tab separated file with the extension .bed and columns chromosome, start, end, t_name.

usage: ./find_promoter.py <ctab>
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv( sys.argv[1], sep = "\t" )

soi_plus = df["strand"] == "+"
soi_minus = df["strand"] == "-"

#
# df_plus = df[coi]
# df_minus = df[coi]
#
# for sample in df[soi_plus]:
#     df_plus["promoter_start"] = df_plus["start"] - 500
#     df_plus["promoter_end"] = df_plus["start"] + 500
# for sample in df[soi_minus]:
#     df_minus["promoter_start"] = df_minus["end"] - 500
#     df_minus["promoter_end"] = df_minus["end"] - 500

df_plus_out = pd.DataFrame()
df_minus_out = pd.DataFrame()

for sample in df[soi_plus]:
    genestart = df["start"][soi_plus]
    df_plus_out["chr"] = df["chr"][soi_plus]
    df_plus_out["start"] = genestart - 500
    df_plus_out["end"] = genestart + 500
    df_plus_out["t_name"] = df["t_name"][soi_plus]

for sample in df[soi_minus]:
    genestart = df["end"][soi_minus]
    df_minus_out["chr"] = df["chr"][soi_minus]
    df_minus_out["start"] = genestart - 500
    df_minus_out["end"] = genestart + 500
    df_minus_out["t_name"] = df["t_name"][soi_minus]
    
#print df_plus_out
#print df_minus_out

df_final = df_plus_out.append(df_minus_out)

only_positives = df_final["start"] >= 0
df_final = df_final[only_positives]

df_final.to_csv( "promoters.bed", "\t", header=False, index=False )