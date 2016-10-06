#!/usr/bin/python2
import base64, binascii, sys

def func(val):
    return base64.b64encode(binascii.unhexlify(s))

s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'


if len(sys.argv) < 2:
    print func(s)
else:
    print(func(sys.argv[1]))





