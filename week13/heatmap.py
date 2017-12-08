#!/usr/bin/env python

'''
./heatmap.py [datafile]
'''

import sys
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
from scipy.cluster.vq import kmeans2
import scipy.stats
import numpy as np
import pandas as pd

data = pd.read_csv(sys.argv[1], "\t", header = 0, index_col = 0)
columns = ["SRR492183", "SRR492189", "SRR492194", "SRR492186", "SRR492190", "SRR492197", "SRR492188", "SRR492193"]
data = data[columns]
data_array = data.as_matrix()

#link_matrix_obs = linkage(data_array,'average')
link_matrix_type = linkage(np.transpose(data_array),'average')

#cluster_obs = leaves_list(link_matrix_obs)
cluster_type = leaves_list(link_matrix_type)

rows = ["Staphylococcus haemolyticus", "Leuconostoc citreum", "Staphylococcus lugdunensis", "Enterococcus faecalis", "Cutibacterium avidum", "Staphylococcus epidermidis", "Staphylococcus aureus", "Anaerococcus prevotii"]

plt.style.use('ggplot')
#============================================================#
# LOAD SOME DATA TO USE

X = data_array[:,cluster_type]
Y = data_array[cluster_obs,:]
#ordered_labelsx = [columns[i] for i in cluster_type]
ordered_labelsy = [rows[i] for i in cluster_obs]

#============================================================#
# CREATE SOME PLOTS

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
	cmap="copper",                             # ... Use the Red-white-blue colormap to assign colors to your pixel values
	vmin=0,                               # ... Set the lowest value to show on the scale
	vmax=m,                                  # ... Set the highest value to show on the scale. Since we are using a 'diverging' colormap, these should match.
	)
plt.grid(False)        # Turn of the grid lines (a feature added automatically by ggplot)
plt.xticks(            # Edit the xticks being shown
	range(X.shape[1]), # ... use the values centered on each column of pixels
	ordered_labelsx,           # ... which corresponds to the indices of our labels
	rotation=50,       # ... and rotate the labels 50 degrees counter-clockwise
	)
plt.yticks(
    range(Y.shape[1]),
    ordered_labelsy,
)         # Edit the ticks on the y-axis to show....NOTHING
plt.colorbar()         # Add a bar to the right side of the plot which shows the scale correlating the colors to the pixel values

# plt.subplots_adjust( # Adjust the spacing of the subplots, to help make everything fit
#     left = 0.05,     # ... the left edge of the left-most plot will be this percent of the way across the width of the plot
#     bottom = 0.15,   # ... the bottom edge of the bottom-most plot will be this percent of the way up the canvas
#     right = 1.0,     # ... the right edge of the right-most plot will be this percent of the way across the width
#     top = 0.95,      # ... the top edge of the top-most plot will be this percent of the way from the bottom
# )

plt.tight_layout()

plt.savefig("test_heatmap.png") # Save the image
plt.close() # Close the canvas