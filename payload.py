a = 'In this letter I make some remarks on a general principle relevant to enciphering in general and my machine.'
b = 'If qualified opinions incline to believe in the exponential conjecture, then I think we cannot afford not to make use of it.'
c = 'The most direct computation would be for the enemy to try all 2^r possible keys, one by one.'
d = 'The significance of this general conjecture, assuming its truth, is easy to see. It means that it may be feasible to design ciphers that are effectively unbreakable.'

a = 'To consider the resistance of an enciphering process to being broken we should assume that at same times the enemy knows everything but the key being used and to break it needs only discover the key from this information.'
b = 'The most direct computation would be for the enemy to try all 2^r possible keys, one by one.'
c = 'An enciphering-deciphering machine (in general outline) of my invention has been sent to your organization.'
d = 'We see immediately that one needs little information to begin to break down the process.'

for s in (a, b, c, d):
    n = len(s)
    b = ((n + 1) // 16 + 1) * 16 + 16
    # print('%3d = %2d + %2d/16' % (n, n // 16, n % 16))
    print('%3d => %3d %s' % (n, b, s[:20]))
