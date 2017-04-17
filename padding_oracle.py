"""
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

    1::  1  1:                                                 20                ' '
     2::  2  2:                                               7320               's '
     3::  3  3:                                             647320              'ds '
     4::  4  4:                                           72647320             'rds '
     5::  5  5:                                         6f72647320            'ords '
     6::  6  6:                                       576f72647320           'Words '
     7::  7  7:                                     20576f72647320          ' Words '
     8::  8  8:                                   6320576f72647320         'c Words '
     9::  9  9:                                 696320576f72647320        'ic Words '
    10:: 10 10:                               67696320576f72647320       'gic Words '
    11:: 11 11:                             6167696320576f72647320      'agic Words '
    12:: 12 12:                           4d6167696320576f72647320     'Magic Words '
    13:: 13 13:                         204d6167696320576f72647320    ' Magic Words '
    14:: 14 14:                       65204d6167696320576f72647320   'e Magic Words '
    15:: 15 15:                     6865204d6167696320576f72647320  'he Magic Words '
    16:: 16 16:                   546865204d6167696320576f72647320 'The Magic Words '
    --------------------------------------------------------------------------------
    The Magic Words are Squeamish Ossifrage\t\t\t\t\t\t\t\t\t

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
    assert False

base = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'
b = len(base)
assert b % 2 == 0, b
n = b // 2
cip = [int(base[2 * i:2 * i + 2], 16) for i in range(n)]
print('cip=%d' % len(cip))
assert txt(cip) == base


def do_block(cip, B):
    N = (B + 1) * 16
    M = B * 16
    cip = cip[:N]
    assert len(cip) == N
    answer = []
    plain = ''
    for pos in range(1, 16 + 1):
        found = False
        orig_g = None
        print('%2d::' % pos, end=' ')
        for n in range(0x100):
            o = M - pos
            h = [n] + list(reversed(answer))
            d = [h[i] ^ cip[M - pos + i] ^ pos for i in range(pos)]
            xcip = cip[:M - pos] + d + cip[M:]
            assert len(xcip) == N, (len(xcip), N, M, pos)
            q = txt(xcip)
            try:
                g, k = query(q)
            except:
                orig_n = n
                g = False
            if g:
                assert not found
                found = True
                answer.append(n)
                a = list(reversed(answer))
                plain = asc(a)
                print('%2d %2d: %50s %18r' % (len(a), len(plain), txt(a), plain))
                break
            # assert k == 403 or g
        if not found:
            assert orig_n is not None
            n = orig_n
            answer.append(n)
            a = list(reversed(answer))
            plain = asc(a)
            print('%2d %2d: %50s %18r' % (len(a), len(plain), txt(a), plain))

    return plain


answers = []
for B in 1, 2, 3:
    a = do_block(cip, B)
    print('-' * 80)
    answers.append(a)
print('=' * 80)
plain = ''.join(answers)
print('%d %r' % (len(plain), plain))
