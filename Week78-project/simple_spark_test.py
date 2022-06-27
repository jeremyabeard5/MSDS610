"""
This can be used to test if your spark installation is working properly.  It's meant to run in Python3.
"""

from pyspark import SparkContext
try:
    sc = SparkContext('local')
except:
    print('using existing spark context')
    sc = SparkContext.getOrCreate()

import random

NUM_SAMPLES = int(1e7)

def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

count = sc.parallelize(range(0, NUM_SAMPLES)).filter(inside).count()

print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))
