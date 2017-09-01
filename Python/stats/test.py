import pylab
import random

## First do a histogram of the true distribution, i.e.,
## uniform integers 1 to 6 inclusive


## Define a method for drawing samples of a given size.

def takeSample(size):
    observedSample = []
    for i in range(size):
        observedSample.append(random.randint(1, 6))
    return pylab.mean(observedSample)


listOfSampleMeans = []


## Build up a deliberately weird distribution
## The weirdVariate method gives one variate from the distribution.

def weirdVariate():
    method = random.randint(1, 5)
    if method == 1:
        variate = 0.0
    elif method == 2:
        variate = random.expovariate(0.2)
    elif method == 3:
        variate = random.uniform(10, 20)
    elif method == 4:
        variate = random.normalvariate(22, 5)
    elif method == 5:
        variate = random.normalvariate(70, 4)
    return variate


def weirdSample(size):
    thisSample = []
    for i in range(size):
        thisSample.append(weirdVariate())
    return pylab.mean(thisSample)


testSample = []
for i in range(10000):
    testSample.append(weirdVariate())

pylab.hist(testSample, bins=30, color="red")
pylab.xlabel('Score', size="x-large")
pylab.ylabel('Count', size="x-large")
pylab.title('10000 variates from a strange multi-modal distribution',
            size='x-large')
pylab.show()

sampleMeans = []
for i in range(10000):
    sampleMeans.append(weirdSample(2))

pylab.hist(sampleMeans, bins=30, color="green")
pylab.xlabel('Sample mean', size="x-large")
pylab.ylabel('Count', size="x-large")
pylab.title('Mean of 10000 samples of size 2 from a strange distribution',
            size='x-large')
pylab.show()

sampleMeans = []
for i in range(10000):
    sampleMeans.append(weirdSample(4))

pylab.hist(sampleMeans, bins=30, color="green")
pylab.xlabel('Sample mean', size="x-large")
pylab.ylabel('Count', size="x-large")
pylab.title('Mean of 10000 samples of size 4 from a strange distribution',
            size='x-large')
pylab.show()

sampleMeans = []
for i in range(10000):
    sampleMeans.append(weirdSample(8))

pylab.hist(sampleMeans, bins=30, color="green")
pylab.xlabel('Sample mean', size="x-large")
pylab.ylabel('Count', size="x-large")
pylab.title('Mean of 10000 samples of size 8 from a strange distribution',
            size='x-large')
pylab.show()
