# -*- coding: utf-8 -*-
"""e <csv> path
        -p disables page level color detection
"""
# TODO
#   Check for duplicates
#   Prettify stdout
#   Improve filter sysntax regex's !@#$ Filtering is broken


from __future__ import division, print_function


def matrix(n):
    return [[0] * n for _ in range(n)]


def checker(n):
    a = matrix(n)
    for y in range(n):
        for x in range(n):
            a[y][x] = (x + y) % 2
    return a


def tohex(row):
    assert len(row) % 8 == 0
    h = len(row) // 8
    out = []
    for i in range(h):
        x = 0
        for j in range(8):
            if row[i * 8 + j]:
                x += 2 ** j
        out.append(x)
    return out


def arrhex(a):
    out = []
    for row in a:
        out.extend(tohex(row))
    return out


def tostr(a):
    for x in a:
        assert isinstance(x, int), (x, type(x))
    s = ''.join('%02x' % x for x in a)
    chunks = [s[i:i + 8] for i in range(0, len(s), 8)]
    lines = [' '.join(chunks[i:i + 8]) for i in range(0, len(chunks), 8)]
    s = '\n'.join(lines)
    return '<%s>' % s


n = 8
a = checker(n)
for row in a:
    print(' ', row)
b = arrhex(a)
print(b)
s = tostr(b)
print('s = %s' % s)
print()
