from __future__ import print_function
import numpy
import argparse
from matplotlib import pyplot


parser = argparse.ArgumentParser(description='Postgres Inserter')
parser.add_argument("-1", "--one", dest="file1", help="The first file to import", required=True)
parser.add_argument("-2", "--two", dest="file2", help="The second file to import", required=True)
args = parser.parse_args()


def floatify(x):
    try:
        y = float(x)
        return y
    except:
        pass


def m_m():
    min_x = min(x)
    min_y = min(y)
    max_x = max(x)
    max_y = max(y)

    min_lowest = min((min_x, min_y))
    max_highest = max((max_x, max_y))
    return (min_lowest, max_highest)


x = []
y = []
infile1 = open(args.file1, "r")
for item in infile1.readlines():
    x.append(floatify(item.strip()))

infile2 = open(args.file2, "r")
for item in infile2.readlines():
    y.append(floatify(item.strip()))

min_max = m_m()
bins = numpy.linspace(min_max[0], min_max[1], 100)
pyplot.hist(x, bins, alpha=0.5, label='x')
pyplot.hist(y, bins, alpha=0.5, label='y')
pyplot.legend(loc='upper right')
pyplot.tight_layout()
pyplot.plot()

fig = pyplot.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('histogram.png', dpi=300)
