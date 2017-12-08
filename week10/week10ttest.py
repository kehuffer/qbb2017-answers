#!/usr/bin/env python

'''
./week10ttest.py [datafile]
'''

import sys
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
from scipy.cluster.vq import kmeans2
import scipy.stats
import numpy as np
import pandas as pd
from itertools import izip as zip, count 

data = pd.read_csv(sys.argv[1], "\t")
data_array = data.as_matrix(columns = ["CFU", "poly", "unk", "int", "mys", "mid"])

link_matrix_obs = linkage(data_array,'average')
link_matrix_type = linkage(np.transpose(data_array),'average')

cluster_obs = leaves_list(link_matrix_obs)
cluster_type = leaves_list(link_matrix_type)

kmeans = kmeans2(data_array[:,0:2], 5)

plt.style.use('ggplot')
#============================================================#
# LOAD SOME DATA TO USE

X = data_array[cluster_obs,:][:,cluster_type]
labels = ["CFU", "poly", "unk", "int", "mys", "mid"]
ordered_labels = [labels[i] for i in cluster_type]

#============================================================#
# CREATE SOME PLOTS

# Start by normalizing the data so each feature can fit on the
##same scale. Basically we are calculating the Z-score for 
##each value based on only the feature it belongs to.
X = (X-np.average(X,axis=0))/np.std(X,axis=0)
# take the z-scores for each column and average the first two stages and last two stages with each other
# then use paired t test to compare early and late P < .05
# then use normalized intensity ratio > 2 or < .5 to pull out genes with significant change
early_avg = np.average(X[:,2:4], axis = 1)
late_avg = np.average(X[:,0:2], axis = 1)
early_late_avg = np.stack((early_avg, late_avg), axis = 1)
#print scipy.stats.ttest_ind(early_late_avg, axis = 1)
ratio = (data_array[:,0] + data_array[:,4]) / (data_array[:,1] + data_array[:,2])
early = np.column_stack((data_array[:,0], data_array[:,4]))
late = np.column_stack((data_array[:,1], data_array[:,2]))
ttest = scipy.stats.ttest_ind(early, late, axis = 1)
# Filter t-test results by p-value using Bonferroni correction
bonpval = 0.05/(len(ttest.pvalue))
bonind = [i for i, j in zip(count(), ttest.pvalue) if j <= bonpval]
bongene = data["gene"][bonind]
print "Significantly different average values for early and late expression: %s" % (bongene)

index_min = min(xrange(len(ratio)), key=ratio.__getitem__)
rel_genes = []
sig_ratio_gene = []
for index, item in enumerate(ratio):
    if item >= 2.0 or item <= 0.5:
        sig_ratio_gene.append((data["gene"][index], item))
        if kmeans[1][index] == kmeans[1][index_min]:
            rel_genes.append(data["gene"][index])
print "The most upregulated gene in late differentiation is %s." %(data["gene"][index_min])
print "\nAll differentially expressed genes, according to ratio:"
print sig_ratio_gene
print "kmeans group: %s" %(kmeans[1][index_min])
print "\nAll genes in k-means group:"
print rel_genes

# Pull out the value with the greatest magnitude, to set the
##scale
m = np.max(np.abs(X))

# Make the heatmap
plt.figure()                                 # Open a blank canvas
plt.title("Heatmap") # Add a title to the top
plt.imshow(                                  # Treat the values like pixel intensities in a picture
	X,                                       # ... Using X as the values
	aspect='auto',                           # ... 'Stretch' the image to fit the canvas, so you don't get a skinny strip that is 4x150 pixels
	interpolation='nearest',                 # ... Don't use any blending between pixel values
	cmap="RdBu",                             # ... Use the Red-white-blue colormap to assign colors to your pixel values
	vmin=-1*m,                               # ... Set the lowest value to show on the scale
	vmax=m,                                  # ... Set the highest value to show on the scale. Since we are using a 'diverging' colormap, these should match.
	)
plt.grid(False)        # Turn of the grid lines (a feature added automatically by ggplot)
plt.xticks(            # Edit the xticks being shown
	range(X.shape[1]), # ... use the values centered on each column of pixels
	ordered_labels,           # ... which corresponds to the indices of our labels
	rotation=50,       # ... and rotate the labels 50 degrees counter-clockwise
	)
plt.yticks([])         # Edit the ticks on the y-axis to show....NOTHING
plt.colorbar()         # Add a bar to the right side of the plot which shows the scale correlating the colors to the pixel values

plt.subplots_adjust( # Adjust the spacing of the subplots, to help make everything fit
    left = 0.05,     # ... the left edge of the left-most plot will be this percent of the way across the width of the plot
    bottom = 0.15,   # ... the bottom edge of the bottom-most plot will be this percent of the way up the canvas
    right = 1.0,     # ... the right edge of the right-most plot will be this percent of the way across the width
    top = 0.95,      # ... the top edge of the top-most plot will be this percent of the way from the bottom
)

plt.savefig("test_heatmap.png") # Save the image
plt.close() # Close the canvas

# ------------------
# k-means scatterplot
plt.figure()
plt.title("k-means")
plt.scatter(data_array[:,0], data_array[:,1], c = kmeans[1])
plt.ylabel("poly expression")
plt.xlabel("CFU expression")
plt.savefig("test_kmeans.png")
plt.close()

# -------------------
# Make the dendrogram
plt.figure()
plt.title("Dendrogram")
#dendrogram(link_matrix_type, labels = [labels[i] for i in cluster_type], leaf_font_size = 8)
dendrogram(link_matrix_type, labels = labels, leaf_font_size = 8)
plt.ylabel("Distance")
plt.xlabel("Population")
plt.savefig("test_dendrogram.png")
plt.close()