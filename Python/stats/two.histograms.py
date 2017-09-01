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


def get_name():
    if '/' in args.file1:
        name1_temp = args.file1.split('/')
        name1 = name1_temp[-1]
    else:
        name1 = args.file1
    if '/' in args.file2:
        name2_temp = args.file2.split('/')
        name2 = name2_temp[-1]
    else:
        name2 = args.file2

    return name1, name2


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

names = get_name()
min_max = m_m()
bins = numpy.linspace(min_max[0], min_max[1], 100)
pyplot.hist(x, bins, alpha=0.5, label=names[0])
pyplot.hist(y, bins, alpha=0.5, label=names[1])
pyplot.legend(loc='upper right')
pyplot.tight_layout()
pyplot.plot()

fig = pyplot.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('histogram.{}.{}.png'.format(names[0], names[1]), dpi=300)
