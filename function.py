import re
from collections import defaultdict
from glob import glob


RE_FUNCTION = re.compile(b'<<.{,900}?/FunctionType\s+(\d)+.{,900}?>>', re.MULTILINE | re.DOTALL)

# text = b'<</FunctionType 0/Size [1365]/Filter /FlateDecode/Length 63 0 R/Order 1/BitsPerSample 8/Domain [0 1]/Range [0 1 0 1 0 1]/Decode [0 1 0 1 0 1]/Encode [0 1364]>>'
# print(RE_FUNCTION.findall(text))


def find_functions(path):
    text = read(path)
    # print('$$$ %d "%s" `%s`' % (len(text), path, text[:100]))
    # o = text.find(b'/FunctionType')
    # print('!!! %d `%s`' % (o, text[o - 10:o + 50]))
    types = defaultdict(list)
    for m in RE_FUNCTION.finditer(text):
        # print('>>>>', m.start(), m.end() - m.start(), m.group(0))
        types[int(m.group(1))].append(m.group(0))
    return types
    # return RE_FUNCTION.findall(text)


def read(path):
    with open(path, 'rb') as f:
        return f.read()


path = '/Users/pcadmin/go-work/src/trust-me/testdata/spool/000010.pdf'
functions = find_functions(path)
functions = defaultdict(set)
n_functions = defaultdict(int)
#for path in glob('/Users/pcadmin/go-work/src/trust-me/testdata/spool/*.pdf'):
for path in glob('/Users/pcadmin/go-work/src/trust-me/testdata/*.pdf'):
    funcs = find_functions(path)
    for k, v in funcs.items():
        n_functions[k] += len(v)
        functions[k] |= set(v)

# print(functions)
for i, func in enumerate(sorted(functions)):
    print('%3d: %d %d %d' % (i, func, n_functions[func], len(functions[func])))

func3 = functions[4]
for i, s in enumerate(sorted(func3)[:5]):
    print('%3d %s' % (i, '-' * 80))
    print(s.decode("cp1252", "ignore"))
