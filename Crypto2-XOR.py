#!/usr/bin/env python3
import os
import random

# with open('flag', 'rb') as data:
#     flag = data.read()
    # assert(flag.startswith(b'AIS3{'))

def extend(key, L):
    kL = len(key)
    return key * (L // kL) + key[:L % kL]

def xor(X, Y):
    return bytes([x ^ y for x, y in zip(X, Y)])

# key = os.urandom(random.randint(8, 12))
# plain = flag + key
# key = extend(key, len(plain))
# cipher = xor(plain, key)

# with open('flag-encrypted', 'wb') as data:
#     data.write(cipher)

data = open('Crypto2-flag-encrypted', 'rb').read()
print(len(data))


key = xor(b'AIS3{', data)
# print(key)
# for i in range(8, 13):
# 	print(xor(data[-i:], key))

for i in range(5):
	temp = xor(data[-10:], key)
	key += bytes([temp[-1]])

key_length = 10
flag_length = 151
# AIS3{xxxxx}1234567890
# 12345xxxxx12345678901

key = extend(key, len(data))

print(xor(data, key))
