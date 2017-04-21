"""
    7a + 23b = 1
    b = (1 - 7a) / 23
"""
from math import floor, ceil


found = False
for a in range(10**6):
    q = (1 - 7 * a) / 23
    b0, b1 = int(floor(q)), int(ceil(q))
    print('a=%d q=%.3f b=[%d,%d]' % (a, q, b0, b1))
    assert 0 <= b1 - b0 <= 1
    for b in range(b0, b1 + 1):
        if 7 * a + 23 * b == 1:
            print('a=%d b=%d' % (a, b))
            found = True
            break
    if found:
        break


