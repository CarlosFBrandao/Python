from os import strerror

try:
    hist = dict()
    for line in open('text.txt', 'rt'):
        for ch in line:
            print(ch, end='')
            if ch != ' ' and ch != '\n' and ch!= '':
                hist[ch.lower()] = hist.get(ch.lower(), 0) +1
except IOError as e:
    print('I/O error ocurred: ', strerror(e.errno))
print('\n\nHistgrama:\n')

for chave in sorted(hist, key = hist.get, reverse=True):
    print(f'{chave} -> {hist[chave]}')