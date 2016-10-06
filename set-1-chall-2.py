#!/usr/bin/python2
import crypto


s = '1c0111001f010100061a024b53535009181c'
x = '686974207468652062756c6c277320657965'

clear, key = map(crypto.hex_to_bytes, (s,x))
result = crypto.bytes_to_hex(crypto.fixed_xor(clear, key))

print result







