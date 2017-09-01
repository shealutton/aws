#!/usr/bin/python

from __future__ import print_function
from optparse import OptionParser
import sys
import numpy


def is_number(s):
    try:
        float(s) # for int, long and float
        return True
    except ValueError:
        try:
            complex(s) # for complex
            return True
        except ValueError:
            return False
    return True


parser = OptionParser()
parser.add_option("-f", "--file", dest="file", help="The file to import")
(options, args) = parser.parse_args(args=None, values=None)

if options.file:
   infile = open(options.file, "r")
else:
   print("missing -f file argument")
   sys.exit(1)

dirtydata=infile.readlines()
data=list()
for index,element in enumerate(dirtydata):
    if is_number(element):
        data.append(float(element.strip()))

### The math starts here ###
frequency, buckets = numpy.histogram(data, bins=20)
ourbin=buckets[1]-buckets[0]
ourmean=numpy.mean(data)
ourmedian=numpy.median(data)
ourmax=numpy.max(data)
ourmin=numpy.min(data)
oursum=numpy.sum(data)
ourrange=ourmax - ourmin
ourlength=len(data)
ourstddev=numpy.std(data)
### Output starts here ###
print("samples:     ", ourlength)
print("min:         ", ourmin)
print("max:         ", ourmax)
print("range:       ", ourrange)
print("sum:         ", oursum)
print("mean:        ", ourmean)
print("median:      ", ourmedian)
print("std dev:     ", ourstddev)
print("bin width:   ", ourbin)
print("      Histogram\n       Bin Frequency  (%)")
digit='%10d'
for i in range(20): # %s substitute out the values and print them
    ourpercent = (float(frequency[i])/float(ourlength))*100
    print(digit % buckets[i], '%-10d' % frequency[i], '%.1f\t' % ourpercent)
