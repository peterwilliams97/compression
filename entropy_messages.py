from math import log2
from collections import defaultdict


def ilog2(x):
    """ 1/log2(x) """
    if x == 0.0:
        return 0.0
    return -log2(x)


def entropy(data):
    return sum(x * ilog2(x) for x in data)


def to_dist(data):
    """ Probability distribution must sum to 1.0"""
    return [x / sum(data) for x in data]


def get_counts(s):
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1
    return [counts[c] for c in sorted(counts)]


messages = [
    'abcdefghijklmnopqrstuvwxyz ',
    'i did but see her passing by',
    'rhythm rhythm rhythm rhythm',
    'banana banana banana banana',
    'eeeeeeeeeeeeeeeeeeeeeeeeeee',
]

for msg in messages:
    data = get_counts(msg)
    data = to_dist(data)
    print('%5.3f "%s"' % (entropy(data), msg))
