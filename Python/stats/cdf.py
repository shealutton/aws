from matplotlib.pyplot import *
from __future__ import print_function
from optparse import OptionParser
import numpy as np
import sys


parser = OptionParser()
parser.add_option("-f", "--file", dest="file", help="The file to import")
(options, args) = parser.parse_args(args=None, values=None)

if options.file:
    infile = open(options.file, "r")
else:
    print("missing -f file argument")
    sys.exit(1)

data = np.loadtxt(infile.readlines())

# Choose how many bins you want here
num_bins = 10000

# Use the histogram function to bin the data
counts, bin_edges = np.histogram(data, bins=num_bins, normed=True)

# Now find the cdf
cdf = np.cumsum(counts)

# And finally plot the cdf
fig = figure(1, figsize=(10,8))
plot(bin_edges[1:], cdf)
fig.savefig('cdf.png', dpi=300)
