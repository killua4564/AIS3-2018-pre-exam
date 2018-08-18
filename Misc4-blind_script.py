# script from yuawn
import os
import re
import base64
from pwn import *

conn = remote("....")

conn.sendlineafter("=", sol) # proof of work

def ppp(n):
	a = hex(n)[2:]
	if len(a) % 2: a = '0' + a
	return ''.join([chr(int(i, 16)) for i in re.findall('..', a)])

def crack(ci, bloc):
	for i in range(127-16, 0, -16):
		for j in range(1 << bloc, -1, -1):
			temp = j << (((i // bloc) + 1) * bloc)
			conn.sendlineafter(":", base64.b64encode(ppp(temp) + ci))
			a = conn.recvline()
			conn.sendlineafter(":", base64.b64encode(ppp(temp ^ flip(i)) + ci))
			b = conn.recvline()
			print(a, b)
	return 1

if __name__ == '__main__':
	ci = ''
	for _ in range(0x10000):
		ci = os.urandom(16)
		if crack(ci, 16):
			print("win!!!!!")
			break
		else: print("try!!!")