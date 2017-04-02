def xor(x, y):
    return [a ^ b for a, b in zip(x, y)]


def from_h(s):
    """Returns list of bytes corresponding to hex string `s`"""
    s = s.replace(' ', '')
    assert len(s) % 2 == 0
    return [int(s[2 * i: 2 * i + 2], 16) for i in range(len(s) // 2)]


def list2str(a):
    strings = ['%02x' % x for x in a]
    if len(strings) > 10:
        strings = strings[:5] + ['...'] + strings[-5:]
    return '[%s]' % ','.join(strings)


a = ("e86d2de2 e1387ae9", "1792d21d b645c008")
b = ("5f67abaf 5210722b", "bbe033c0 0bc9330e")
c = ("7c2822eb fdc48bfb", "325032a9 c5e2364b")
d = ("7b50baab 07640c3d", "ac343a22 cea46d60")

pairs = [(from_h(s1), from_h(s2)) for s1, s2 in (a, b, c, d)]

for i, (s1, s2) in enumerate(pairs):
    s12 = xor(s1, s2)
    print('%2d: %s %s %s' % (i, list2str(s1), list2str(s2), list2str(s12)))
