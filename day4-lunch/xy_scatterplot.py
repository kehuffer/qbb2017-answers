#!/usr/bin/env python

"""
Usage: ./xy_scatterplot.py <x_plot> <y_plot> <prefix>
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x_df = pd.read_csv( sys.argv[1], sep = "\t" )
y_df = pd.read_csv( sys.argv[2], sep = "\t" )

x_log = np.log(x_df["FPKM"]+1)
y_log = np.log(y_df["FPKM"]+1)

y_fit = np.polyfit( x_log, y_log, 1)
print y_fit

plt.figure()
plt.scatter(x_log, y_log, alpha = 0.5)
#plt.plot(x_log, ((x_log*y_fit[0])+y_fit[1]))
new_x = np.linspace(np.min(x_log), np.max(x_log), 100)
new_y = new_x * y_fit[0] + y_fit[1]

plt.plot(new_x, new_y, "r")

plt.title("FPKM values of SRR072893 and SRR072915")

plt.xlabel("SRR072893 (ln(FPKM))")
plt.ylabel("SRR072915 (ln(FPKM))")
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.savefig(sys.argv[3] + ".png")
plt.close()