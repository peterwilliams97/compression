"""
    Using http://www.macfreek.nl/memory/images/EN-Letters.txt
"""

import csv


letter_frequencies = {}


# Read space and letter frequencies from file
with open('EN-Letters.txt', 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter='\t')
    next(r)
    for row in r:
        c = row[-1]
        f = float(row[0])
        if f > 0.0:
            letter_frequencies[c] = f


# Guess punctuation and digit frequencies
A = letter_frequencies['E'] * 0.8
B = letter_frequencies['B'] * 0.01

for c in ''',.-"_')(;=:/*!?$>{}[]\+|&<%@#^`~''':
    letter_frequencies[c] = A
    A *= 0.4


for c in '0123456789':
    letter_frequencies[c] = B
