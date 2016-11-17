from Crypto.Util.strxor import strxor
from binascii import hexlify, unhexlify
import string

def score(data):
    scr = filter(lambda x: 'a' <= x <= 'z' or 'A' <= x <= 'Z' or x == ' ',
                 [i for i in data])
    return float(len(scr)) / len(data)


a = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
a = unhexlify(a)


l = []
m = []

for i in range(65, 123):
    temp = ''
    for x in a:
        s = strxor(x, chr(i))
        temp += s
    temp += '\n'
    m.append(score(temp))
    l.append(temp)

print(l[m.index(max(m))])

