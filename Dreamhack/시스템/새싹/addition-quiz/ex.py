from pwn import *

r = remote("host3.dreamhack.games", 22009)

n1 = int(r.recvuntil(b'+', drop=True))
n2 = int(r.recvuntil(b'=?\n', drop=True))

r.sendline(str(n1 + n2).encode())

r.interactive()