#!/usr/bin/env python

'''
./runonfiles.py <ref.fa> <created_name.vcf> <histogram.png>
'''

import os
import sys
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(0, '/Users/cmdb/qbb2017-answers/week3/PyVCF')
import vcf

ref = sys.argv[1]
inputlist = ['A01_09.fastq', 'A01_11.fastq', 'A01_23.fastq', 'A01_24.fastq', 'A01_27.fastq', 'A01_31.fastq', 'A01_35.fastq', 'A01_39.fastq', 'A01_62.fastq', 'A01_63.fastq']

for item in inputlist:
    os.system("bwa mem -R '@RG\\tID:%s\\tSM:%s' %s %s > %s.sam" % (item, item, ref, item, item))
    os.system("samtools sort -o %s.sorted.bam %s.sam" % (item, item))
    os.system("samtools index -b %s.sorted.bam" % (item))

os.system("freebayes -f %s *.sorted.bam > results.vcf" % (ref))
os.system("vcffilter results.vcf -f \"QUAL > 4000\" > %s" % (sys.argv[2]))

frequencies_list = []

vcf_reader = vcf.Reader(open("results.vcf", 'r'))
for record in vcf_reader:
    for freq in record.INFO['AF']:
        frequencies_list.append(freq)
print frequencies_list
bins_list = np.arange(0.0, 1.0, 0.02)
plt.figure()
plt.hist(frequencies_list, bins_list)
plt.title("Allele Frequency Spectrum")
plt.xlabel("Allele Frequency")
plt.ylabel("Number of Alleles")
plt.savefig(sys.argv[3])
plt.close()

os.system("SnpEff Saccharomyces_cerevisiae results.vcf > results.ann.vcf")
os.system("SnpEff Saccharomyces_cerevisiae %s > filteredresults.ann.vcf" % (sys.argv[2]))

vcf_reader_ann = vcf.Reader(open("filteredresults.ann.vcf", 'r'))
for record in vcf_reader_ann:
    for annot in record.INFO['ANN']:
        print record.CHROM, record.POS, record.REF, record.ALT, annot