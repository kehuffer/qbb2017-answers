#!/usr/bin/env python

'''
./week8_python.py [ctcf_peaks.tsv][primers.bed]
'''

import numpy
import pandas
import sys

data = numpy.load('./week8_enrich.heat.npz')
ctcf = pandas.read_csv(sys.argv[1], sep = '\t', header = 0, names = ['Chromosome', 'Position', 'Peak_score', 'Tags_CTCF', 'Tags_IgG'])
primers = pandas.read_csv(sys.argv[2], sep = '\t', header = 0, names = ['chr', 'start', 'stop', 'score', 'name', 'strand', 'gc'])

forprimernames = primers['score'][:511]
revprimernames = primers['score'][511:]

ctcfX = ctcf[ctcf['Chromosome']=='chrX']

forwardbool = numpy.array([], dtype = bool)
reversebool = numpy.array([], dtype = bool)
for item in data['0.forward']:
    hasctcf = False
    for position in ctcfX['Position']:
        if ((position >= item[0]) & (position <= item[1])):
            hasctcf = True
            break
    forwardbool = numpy.append(forwardbool, hasctcf)
for item in data['0.reverse']:
    hasctcf = False
    for position in ctcfX['Position']:
        if ((position >= item[0]) & (position <= item[1])):
            hasctcf = True
            break
    reversebool = numpy.append(reversebool, hasctcf)

transposed = numpy.transpose(reversebool)
    
compressed1 = data['0.enrichment'][forwardbool]
compressed2 = numpy.transpose(compressed1)
compressed3 = compressed2[reversebool]
compressed4 = numpy.transpose(compressed3)
for1 = data['0.forward'][forwardbool]
rev1 = data['0.reverse'][reversebool]
forname = forprimernames[forwardbool]
revname = revprimernames[reversebool]
formaxpartner = numpy.argmax(compressed4, axis = 1)
revmaxpartner = numpy.argmax(compressed4, axis = 0)
forname = forname.reset_index()['score']
revname = revname.reset_index()['score']

for index, item in enumerate(formaxpartner):
    print "CTCF-containing fragment: %s, Coordinates: %s, Strongest CTCF-containing partner: %s, Coordinates: %s, Enrichment: %s" % (forname[index], for1[index], revname[item], rev1[item], compressed4[index,item])
for index, item in enumerate(revmaxpartner):
    print "CTCF-containing fragment: %s, Coordinates: %s, Strongest CTCF-containing partner: %s, Coordinates: %s, Enrichment: %s" % (revname[index], rev1[index], forname[item], for1[item], compressed4[item,index])
