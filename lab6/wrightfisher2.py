#!/usr/bin/env python

'''
./wrightfisher2.py [datafile]
'''

import numpy.random
import matplotlib.pyplot as plt

def generatehistogram(pop, iprob, trials):
    gentofix = []
    n = 2*pop
    for k in range(trials):
        p = iprob
        fixgen = 0
        while True:
            allele = numpy.random.binomial(n, p)
            #print "allele: %d, p: %f" % (allele, p)
            if allele == 0 or allele == n:
                break
            p = float(allele)/float(n)
            fixgen += 1
        gentofix.append(fixgen)
    return gentofix
    
def generateselectionhistogram(pop, iprob, trials, coefficient):
    gentofix = []
    n = 2*pop
    i = iprob * n
    p = i*float(1+coefficient)/float(n-i+(i*float(1+coefficient)))
    for k in range(trials):
        p = i*float(1+coefficient)/float(n-i+(i*float(1+coefficient)))
        fixgen = 0
        while True:
            allele = numpy.random.binomial(n, p)
            #print "allele: %d, p: %f" % (allele, p)
            if allele == 0 or allele == n:
                break
            i = allele
            p = i*float(1+coefficient)/float(n-i+(i*float(1+coefficient)))
            fixgen += 1
        gentofix.append(fixgen)
    return gentofix

# ------------------------------------------------------
# PART 1
iprob = 0.5 # probability of A
pop = 100 # number of individuals
n = 2*pop # number of alleles
p = iprob
trials = 1000
     
part1 = generatehistogram(pop, iprob, trials)

average = numpy.mean(part1)

plt.figure()                  # Open blank canvas
plt.hist(part1, bins = 100)            # Generate a histogram of the data, with defaul settings
plt.ylabel("Frequency")
plt.xlabel("Generations to Fixation")
plt.title("Part I\nGenerations to Fixation")
plt.savefig("part1.png")    # Save the figure
plt.close()                   # Close the canvas
print "part1 complete"

# ------------------------------------------------------
# PART 2
populations = numpy.linspace(100,1000000,10)
fewertrials = trials/10
fixtimepop = []

for population in populations:
    part2 = generatehistogram(population, iprob, fewertrials)
    average = numpy.mean(part2)
    fixtimepop.append(average)

plt.figure()
plt.scatter(populations,fixtimepop)
plt.xlabel("Population")
plt.ylabel("Average Generations to Fixation")
plt.title("Part II\nPopulation Dependence")
plt.savefig("part2.png")
plt.close()
print "part2 complete"

# ------------------------------------------------------
# PART 3

probabilities = numpy.linspace(0,1,20)
fixtimeprob = []

for probability in probabilities:
    part3 = generatehistogram(pop, probability, trials)
    average = numpy.mean(part3)
    fixtimeprob.append(average)
    
plt.figure()
plt.scatter(probabilities,fixtimeprob)
plt.xlabel("Starting Allele Frequency")
plt.ylabel("Average Generations to Fixation")
plt.title("Part III\nProbability Dependence")
plt.savefig("part3.png")
plt.close()
print "part3 complete"
# ------------------------------------------------------
# PART 4

coefficients = numpy.linspace(-1,1,20)
fixtimecoeff = []

for coefficient in coefficients:
    part4 = generateselectionhistogram(pop, iprob, trials, coefficient)
    average = numpy.mean(part4)
    fixtimecoeff.append(average)
    
plt.figure()
plt.scatter(coefficients, fixtimecoeff)
plt.xlabel("Selection Coefficient")
plt.ylabel("Average Generations to Fixation")
plt.title ("Part IV\nSelection Coefficient Dependence")
plt.savefig("part4.png")
plt.close()
print "part4 complete"