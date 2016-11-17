from Crypto.Util.strxor import strxor
from binascii import hexlify, unhexlify

a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'

ans = hexlify(strxor(unhexlify(a), unhexlify(b)))

print(ans)
