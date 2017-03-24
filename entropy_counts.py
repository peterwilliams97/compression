from math import log2
from collections import defaultdict


def list2str(a):
    strings = ['%.2f' % x for x in data]
    if len(strings) > 10:
        strings = strings[:5] + ['...'] + strings[-5:]
    return '[%s]' % ','.join(strings)


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


counts = [
    [1] * 96,  # English language
    [0.1] * 10,
    [0.25] * 4,
    [0.33, 0.33, 0.33],
    [0.5, 0.25, 0.25],
    [0.8, 0.1, 0.1],
    [1.0, 0.0, 0.0]
]

for data in counts:
    data = to_dist(data)
    print('%5.3f %s' % (entropy(data), list2str(data)))
