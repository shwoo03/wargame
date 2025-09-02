#!/usr/bin/env python3

hex_list = [(hex(i)[2:].zfill(2).upper()) for i in range(256)]

with open('flag.png', 'rb') as f:
    plain_s = f.read()

# 2개씩 잘라서 16진수 문자열로 변환 
plain_list = [hex(i)[2:].zfill(2).upper() for i in plain_s]

enc_list = list(range(len(plain_list)))

for i in range(len(plain_list)):
    # 16진수 문자 한개 들고오기
    hex_b = plain_list[i]

    # 16진수 문자 인덱스 찾기
    index = hex_list.index(hex_b)

    # 인덱스에 128 더하고 mod 연산
    enc_list[i] = hex_list[(index + 128) % len(hex_list)]

enc_list = ''.join(enc_list)

with open('encfile', 'w', encoding='utf-8') as f:
    f.write(enc_list)
