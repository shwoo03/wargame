from pwn import *

p = remote("host8.dreamhack.games", 9712)

for i in range(50):
    line = p.recvline().decode().strip()
    split_line = line.split("+")
    num1 = int(split_line[0])
    num2 = int(split_line[1].split("=?")[0])
    result = num1 + num2

    p.sendline(str(result).encode())

flag = p.recvline()
p.interactive()

print(flag.decode())