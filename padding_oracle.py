"""
    ** 73 "s"
    ** 7073 "ps"
    ** 717073 "qps"
    ** 76717073 "vqps"
    ** 7776717073 "wvqps"
    ** 747776717073 "twvqps"
    ** 75747776717073 "utwvqps"
    ** 7a75747776717073 "zutwvqps"
    ** 7b7a75747776717073 "{zutwvqps"
    ** 787b7a75747776717073 "x{zutwvqps"
    ** 79787b7a75747776717073 "yx{zutwvqps"
    ** 7e79787b7a75747776717073 "~yx{zutwvqps"
    ** 7f7e79787b7a75747776717073 "~yx{zutwvqps"
    ** 7c7f7e79787b7a75747776717073 "|~yx{zutwvqps"
    ** 7d7c7f7e79787b7a75747776717073 "}|~yx{zutwvqps"
    ** 627d7c7f7e79787b7a75747776717073 "b}|~yx{zutwvqps"

    **  1: 73                                       "s"
    **  2: 7073                                     "ps"
    **  3: 717073                                   "qps"
    **  4: 76717073                                 "vqps"
    **  5: 7776717073                               "wvqps"
    **  6: 747776717073                             "twvqps"
    **  7: 75747776717073                           "utwvqps"
    **  8: 7a75747776717073                         "zutwvqps"
    **  9: 7b7a75747776717073                       "{zutwvqps"
    ** 10: 787b7a75747776717073                     "x{zutwvqps"
    ** 11: 79787b7a75747776717073                   "yx{zutwvqps"
    ** 12: 7e79787b7a75747776717073                 "~yx{zutwvqps"
    ** 13: 7f7e79787b7a75747776717073               "~yx{zutwvqps"
    ** 14: 7c7f7e79787b7a75747776717073             "|~yx{zutwvqps"
    ** 15: 7d7c7f7e79787b7a75747776717073           "}|~yx{zutwvqps"
    ** 16: 627d7c7f7e79787b7a75747776717073         "b}|~yx{zutwvqps"
    ** 17: 63627d7c7f7e79787b7a75747776717073       "cb}|~yx{zutwvqps"
    ** 18: 6063627d7c7f7e79787b7a75747776717073     "`cb}|~yx{zutwvqps"
    ** 19: 616063627d7c7f7e79787b7a75747776717073   "a`cb}|~yx{zutwvqps"
    ** 20: 66616063627d7c7f7e79787b7a75747776717073 "fa`cb}|~yx{zutwvqps"
    ** 21: 6766616063627d7c7f7e79787b7a75747776717073 "gfa`cb}|~yx{zutwvqps"
    ** 22: 646766616063627d7c7f7e79787b7a75747776717073 "dgfa`cb}|~yx{zutwvqps"
    ** 23: 65646766616063627d7c7f7e79787b7a75747776717073 "edgfa`cb}|~yx{zutwvqps"
    ** 24: 6a65646766616063627d7c7f7e79787b7a75747776717073 "jedgfa`cb}|~yx{zutwvqps"
    ** 25: 6b6a65646766616063627d7c7f7e79787b7a75747776717073 "kjedgfa`cb}|~yx{zutwvqps"
    ** 26: 686b6a65646766616063627d7c7f7e79787b7a75747776717073 "hkjedgfa`cb}|~yx{zutwvqps"
    ** 27: 69686b6a65646766616063627d7c7f7e79787b7a75747776717073 "ihkjedgfa`cb}|~yx{zutwvqps"
    ** 28: 6e69686b6a65646766616063627d7c7f7e79787b7a75747776717073 "nihkjedgfa`cb}|~yx{zutwvqps"
    ** 29: 6f6e69686b6a65646766616063627d7c7f7e79787b7a75747776717073 "onihkjedgfa`cb}|~yx{zutwvqps"
    ** 30: 6c6f6e69686b6a65646766616063627d7c7f7e79787b7a75747776717073 "lonihkjedgfa`cb}|~yx{zutwvqps"
    ** 31: 6d6c6f6e69686b6a65646766616063627d7c7f7e79787b7a75747776717073 "mlonihkjedgfa`cb}|~yx{zutwvqps"
    ** 32: 526d6c6f6e69686b6a65646766616063627d7c7f7e79787b7a75747776717073 "Rmlonihkjedgfa`cb}|~yx{zutwvqps"

     1  1:                                                 73                's'
     2  2:                                               4f73               'Os'
     3  3:                                             204f73              ' Os'
     4  4:                                           68204f73             'h Os'
     5  5:                                         7368204f73            'sh Os'
     6  6:                                       697368204f73           'ish Os'
     7  7:                                     6d697368204f73          'mish Os'
     8  8:                                   616d697368204f73         'amish Os'
     9  9:                                 65616d697368204f73        'eamish Os'
    10 10:                               7565616d697368204f73       'ueamish Os'
    11 11:                             717565616d697368204f73      'queamish Os'
    12 12:                           53717565616d697368204f73     'Squeamish Os'
    13 13:                         2053717565616d697368204f73    ' Squeamish Os'
    14 14:                       652053717565616d697368204f73   'e Squeamish Os'
    15 15:                     72652053717565616d697368204f73  're Squeamish Os'
    16 16:                   6172652053717565616d697368204f73 'are Squeamish Os'

"""

import urllib
import urllib.parse
import urllib.request
import urllib.error


TARGET = 'http://crypto-class.appspot.com/po?er='
# --------------------------------------------------------------
# padding oracle
# --------------------------------------------------------------


def txt(cip):
    return ''.join('%02x' % x for x in cip)


def asc(a):
    return ''.join(chr(x) for x in a)


def query(q):
    target = TARGET + urllib.parse.quote(q)  # Create query URL
    # print('-' * 80)
    # print(target)

    try:
        r = urllib.request.urlopen(target)        # Wait for response
    except urllib.error.URLError as e:
        # print("We got: %d '%s'" % (e.code, e.reason))   # Print response code
        good = e.code == 404            # True => good padding
        return good, e.code
    print('-' * 80)
    print(r)
    assert False, "Can't happen"

base = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'
b = len(base)
assert b % 2 == 0, b
n = b // 2
cip = [int(base[2 * i:2 * i + 2], 16) for i in range(n)]
# print(n)
# print(base)
# print(txt(cip))
assert txt(cip) == base
# query(txt(cip))
N = 48
M = N - 16
cip = cip[:N]
# print(query(txt(cip)))
# assert False

answer = []
for pos in range(1, M + 1):
    found = False
    print('%2d::' % pos, end=' ')
    for n in range(0x100):
        o = M - pos
        # d = [n ^ cip[i] ^ pos for i in range(o, M)]
        # h = list(reversed(answer + [n]))
        h = [n] + list(reversed(answer))
        # h = answer + [n]
        # d = [h[i - o] ^ cip[i] ^ pos for i in range(o, M)]
        d = [h[i] ^ cip[M - pos + i] ^ pos for i in range(pos)]
        # d = [h[i] ^ cip[M - 1 - i] ^ pos for i in range(pos)]
        xcip = cip[:M - pos] + d + cip[M:]
        assert len(xcip) == N, len(xcip)
        q = txt(xcip)
        g, k = query(q)
        # print('0x%02x 0x%02x %d - %s %s - %d %s' % (pos, n, o, txt(cip[o:32]), txt(d), k, g))
        if g:
            assert not found
            found = True
            answer.append(n)
            a = list(reversed(answer))
            print('%2d %2d: %50s %18r' % (len(a), len(asc(a)), txt(a), asc(a)))
            # for _ in range(3):
            #     g, _ = query(q)
            #     assert g
            break
        assert k == 403 or g
    assert found
