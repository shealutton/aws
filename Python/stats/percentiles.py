from __future__ import print_function
from optparse import OptionParser
import numpy as np

parser = OptionParser()
parser.add_option("-f", "--file", dest="file", help="The file to import")
(options, args) = parser.parse_args(args=None, values=None)

if options.file:
    infile = open(options.file, "r")
else:
    print("missing -f file argument")
    sys.exit(1)

data = np.loadtxt(infile.readlines())

print('\nSamples:', len(data))
print('Standard Deviation:', np.std(data))
print('Percentiles')
print('  0%', np.percentile(data, 0))
print(' 10%', np.percentile(data, 10))
print(' 20%', np.percentile(data, 20))
print(' 30%', np.percentile(data, 30))
print(' 40%', np.percentile(data, 40))
print(' 50%', np.percentile(data, 50))
print(' 60%', np.percentile(data, 60))
print(' 70%', np.percentile(data, 70))
print(' 80%', np.percentile(data, 80))
print(' 90%', np.percentile(data, 90))
print(' 95%', np.percentile(data, 95))
print(' 99%', np.percentile(data, 99))
print('100%', np.percentile(data, 100), '\n')
