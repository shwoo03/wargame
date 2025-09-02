with open('./encfile', 'r') as f:
    enc_s = f.read().strip()

# 2글자씩 끊어서 16진수 → int 변환
enc_list = [int(enc_s[i:i+2], 16) for i in range(0, len(enc_s), 2)]

# 복호화: (값 - 128) mod 256
plain_list = [(x - 128) % 256 for x in enc_list]

# 바이트로 변환
plain_bytes = bytes(plain_list)

with open('dec_flag.png', 'wb') as f:
    f.write(plain_bytes)