from pwn import *

p = remote("host1.dreamhack.games", 15762)

line = p.recvuntil(b"Random number: ") 
random_num = p.recvline() 
random_num = int(random_num.strip(), 16)

p.recvuntil(b"Input? ")

secret_string = "a0b4c1d7"
reversed_secret = secret_string[::-1]
v_target = int(reversed_secret, 16)
answer = v_target ^ random_num
decimal_num = str(answer)

p.sendline(decimal_num.encode())
print(p.recvall().decode())