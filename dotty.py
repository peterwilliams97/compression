# -*- coding: utf-8 -*-
"""
    16, 16].int64
    [[0 0 1 0 1 1 1 0 1 0 0 0 0 1 1 0]
     [1 1 1 0 0 0 1 0 0 1 1 1 1 0 1 0]
     [1 0 0 1 1 1 0 1 0 0 1 0 1 1 0 1]
     [0 1 0 1 0 0 1 0 1 1 0 1 0 0 1 0]
     [0 0 1 1 1 0 1 0 1 0 0 1 0 1 0 1]
     [1 0 1 0 1 0 0 1 0 1 0 1 1 0 1 0]
     [1 1 0 1 0 1 1 1 0 1 1 0 1 0 0 0]
     [0 0 1 0 1 0 0 0 1 0 1 0 1 0 1 1]
     [1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 0]
     [0 1 0 1 0 1 1 0 1 0 0 1 0 1 1 1]
     [1 0 1 0 0 0 1 0 0 1 0 1 1 1 0 1]
     [0 1 1 0 1 0 1 1 0 1 0 1 0 0 1 0]
     [1 0 0 0 1 1 0 1 0 1 1 0 1 0 1 0]
     [1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1]
     [0 0 1 1 0 1 1 1 1 0 0 1 0 1 1 0]
     [1 1 0 0 1 0 0 0 0 1 0 1 1 0 1 0]]
    [116, 97, 71, 94, 185, 180, 74, 75, 92, 169, 149, 90, 235, 22, 20, 213, 85, 37, 106, 233, 69, 186, 214, 74, 177, 86, 85, 165, 236, 105, 19, 90]
    s = <7461475e b9b44a4b 5ca9955a eb1614d5 55256ae9 45bad64a b15655a5 ec69135a>
"""
from __future__ import division, print_function
import numpy as np
import random

np.set_printoptions(threshold=64*65, linewidth=200)


def b2x2():
    b = []
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            xj = j % 2
            yj = j // 2
            xi = i % 2
            yi = i // 2
            a = np.zeros((2, 2), dtype=int)
            a[xi, yi] = 1
            a[xj, yj] = 1
            b.append(a)
    return b


def block(n, b):
    assert n % 2 == 0
    a = np.zeros((n // 2, n // 2), dtype=int)
    lut = [i % len(b) for i in range(n * n // 4)]
    random.shuffle(lut)

    def ind(x, y):
        return lut[y * n // 2 + x]

    for y in range(n // 2):
        for x in range(n // 2):
            k = ind(x, y)
            while True:
                ok = (x == 0 or k != a[y, x - 1]) and (y == 0 or k != a[y - 1, x])
                if ok:
                    break
                k = random.randint(0, len(b) - 1)
            a[y, x] = k
    return a


def matrix(n):
    assert n % 2 == 0
    a = np.zeros((n, n), dtype=int)
    b = b2x2()
    c = block(n, b)

    for y in range(n // 2):
        for x in range(n // 2):
            a[y * 2:y * 2 + 2, x * 2:x * 2 + 2] = b[c[y, x]]
    return a


def fix(a):
    n = a.shape[0]

    # a9 = np.empty((n * 3, n * 3), dtype=int)
    # for y in range(3):
    #     for x in range(3):
    #         a9[y * n:(y + 1) * n, x * n:(x + 1) * n] = a

    def m(i):
        return i % n

    def S(a):
        return set(a.flatten().tolist())

    def neig(y, x):
        y1 = min(y + 2, n)
        x1 = min(x + 2, n)
        s = S(a[y:y1, x:x1])
        if y + 2 > n:
            s |= S(a[0: m(y + 2), x:x1])
        if x + 2 > n:
            s |= S(a[y:y1, 0:m(x + 2)])
        if y + 2 > n and x + 2 > n:
            s |= S(a[0:m(y + 2), 0:m(x + 2)])

        return len(s)

    good = False
    for y in range(n):
        for x in range(n):
            if neig(y, x) > 1:
                continue
            # print('**1',)
            a[y, m(x + 1) % n], a[y, m(x + 2)] = a[y, m(x + 2)], a[y, m(x + 1)]
            if neig(y, x) > 1:
                continue
            # print('**2')
            a[y, m(x + 1)], a[y, m(x + 2)] = a[y, m(x + 2)], a[y, m(x + 1)]
            if neig(y, x) > 1:
                continue
            # print('**3')
            a[m(y + 1), m(x + 1)], a[m(y + 1), m(x + 2)] = a[m(y + 1), m(x + 2)], a[m(y + 1), m(x + 1)]
            if neig(y, x) > 1:
                continue
            # print('**4')
            a[m(y + 1), m(x + 1)], a[m(y + 1), m(x + 2)] = a[m(y + 1), m(x + 2)], a[m(y + 1), m(x + 1)]
            if neig(y, x) > 1:
                continue
            # print('**5')
            a[m(y + 1), m(x + 1)], a[m(y + 2), m(x + 2)] = a[m(y + 2), m(x + 2)], a[m(y + 1), m(x + 1)]
            if neig(y, x) > 1:
                continue
            # print('***')
            good = True

    return a, good


def runs(a):
    n = a.shape[0]
    assert n >= 8
    r = []
    bad = 0
    for x0 in range(-n, n):
        u = 1
        b = [(0, x0)]
        k0 = -1
        # print('!', x0)
        for z in range(1, 2*n):
            x = x0 + z
            y = z
            # print('$', y, x)
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            k = a[y, x]
            if k == k0:
                b.append((y, x))
                u += 1
                # print([y, x], k)
            else:
                r.append(u)
                u = 1
                k0 = k
        r.append(u)

    for x0 in range(n, 2 * n):
        u = 0
        k0 = -1
        # print('!', x0)
        for z in range(1, 2 * n):
            x = x0 - z
            y = z
            # print('$', y, x)
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            k = a[y, x]
            if k == k0:
                u += 1
                # print([y, x], k)
            else:
                r.append(u)
                u = 1
                k0 = k
        r.append(u)

    for x0 in range(n):
        u = 1
        k0 = a[0, x0]
        # print('!!!!!', x0)
        for y in range(1, n):
            k = a[y, x0]
            if k == k0:
                u += 1
                # print([y, x], k)
            else:
                r.append(u)
                # print('#', u)
                u = 1
                k0 = k
        r.append(u)

    for y0 in range(n):
        u = 1
        k0 = a[y0, 0]
        # print('!', x0)
        for x in range(1, n):
            k = a[y0, x]
            if k == k0:
                u += 1
                # print([y, x], k)
            else:
                r.append(u)
                u = 1
                k0 = k
        r.append(u)


    # print(r)
    return max(r)


def checker(n):
    best_a = None
    best_run = n + 1
    for j in range(10000):
        a = matrix(n)
        for i in range(25):
            # print('-' * 20, i)
            a, good = fix(a)
            if good:
                break
        print(type(a))
        r = runs(a)
        if r < best_run:
            best_run = r
            best_a = a
        print('run %d: %d %d' % (j, r, best_run))
        if best_run <= 3:
            break
    print('%s.%s' % (list(a.shape), a.dtype))
    # for y in range(n):
    #     for x in range(n):
    #         a[y, x] = (x + y) % 2
    return best_a


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


random.seed(114)
n = 16
a = checker(n)
print(a)
# for row in a:
#     print(' ', row)
b = arrhex(a)
print(b)
s = tostr(b)
print('s = %s' % s)
print()
