from __future__ import print_function
import random
import numpy
import argparse
from matplotlib import pyplot


parser = argparse.ArgumentParser(description='Central Limit Theorem')
parser.add_argument("-p", "--percentile", dest="percentile", help="Eliminate upper bound outliers by specifying a %ile < 100")
parser.add_argument("-s", "--samplesize", dest="sample", help="The percentile of samples to keep from a distribution")
parser.add_argument("-f", "--inputfile", dest="infile", help="Input file", required=True)
args = parser.parse_args()

if args.sample:
    sample_size = int(args.sample)
else:
    sample_size = 8

if args.percentile:
    percentile = int(args.percentile) / 100
else:
    percentile = 1


def sort_and_sample(raw_data):
    if percentile == 1:
        return raw_data
    else:
        sorted_data = sorted(raw_data)
        position = int(round(len(sorted_data) * percentile, 0))
        sorted_data = sorted_data[:position]
        return sorted_data


def floatify(z):
    try:
        y = float(z)
        return y
    except:
        pass


def take_sample(data, size):
    observed_sample = []
    for sample in range(size):
        observed_sample.append(random.sample(data, size))
    return numpy.mean(observed_sample)


def get_name():
    if '/' in args.infile:
        name = args.infile.split('/')
        return name[-1]
    else:
        return args.infile


def main():
    x = []
    xSampleMeans = []

    infile1 = open(args.infile, "r")
    data = infile1.readlines()
    for item in data:
        x.append(floatify(item))

    x = sort_and_sample(x)
    for i in range(10000):
        xSampleMeans.append(take_sample(x, sample_size))

    bins = numpy.linspace(min(xSampleMeans), max(xSampleMeans), 100)
    pyplot.hist(xSampleMeans, bins, alpha=0.5, label='10k samples of {}'.format(sample_size))
    pyplot.legend(loc='upper right')
    pyplot.tight_layout()
    #pyplot.plot()
    #pyplot.show()

    fig = pyplot.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('clt.histogram.{}.sample{}.png'.format(get_name(), sample_size), dpi=300)


if __name__ == '__main__':
    main()
