#!/usr/bin/env python

"""
./phenotypeqa.py
"""

import sys
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

phenofilelist = []
for root, dirs, files in os.walk('/Users/cmdb/qbb2017-answers/week4'):
    for file in files:
        if file.endswith('.assoc.linear'):
            phenofilelist.append(file)

for filename in phenofilelist:
    
    openedfile = pd.read_csv(open(filename), delim_whitespace = True)
    filenameparts = filename.split('.')
    condition = filenameparts[1]
    
    df = pd.DataFrame({'minuslog10pvalue' : -np.log10(openedfile['P']), 'chromosome' : openedfile['CHR']})
    df.chromosome = df.chromosome.astype('category')

    df['ind'] = range(len(df))
    df_grouped = df.groupby(('chromosome'))
    
    colorlist = []
    for index, row in df.iterrows():
        if row['minuslog10pvalue'] >= 5:
            colorlist.append('red')
        elif row['chromosome'] == 'chrI' or row['chromosome'] == 'chrIII' or row['chromosome'] == 'chrIX' or row['chromosome'] == 'chrV' or row['chromosome'] == 'chrVII' or row['chromosome'] == 23 or row['chromosome'] == 'chrXII' or row['chromosome'] == 'chrXIV' or row['chromosome'] == 'chrXVI':
            colorlist.append('black')
        else:
            colorlist.append('grey')
    x_labels = []
    x_labels_pos = []
    for num, (name, group) in enumerate(df_grouped):
        x_labels.append(name)
        x_labels_pos.append((group['ind'].iloc[-1] - (group['ind'].iloc[-1] - group['ind'].iloc[0])/2))
    
    plt.figure()
    plt.scatter(x = df['ind'], y = df['minuslog10pvalue'], color = colorlist)
    plt.xticks(x_labels_pos, x_labels, rotation = 'vertical')
    plt.xlabel("Chromosome")
    plt.ylabel("-log10(p-value)")
    plt.title("Manhattan Plot\n%s"% (condition))
    plt.tight_layout()
    plt.savefig('%s.png' % (condition))
    plt.close()