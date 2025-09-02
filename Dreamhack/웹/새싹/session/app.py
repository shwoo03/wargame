#!/usr/bin/python3
from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)

try:
    FLAG = open('./flag.txt', 'r').read()
except:
    FLAG = '[**FLAG**]'

# ID, PW 딕셔너리 
users = {
    'guest': 'guest',
    'user': 'user1234',
    'admin': FLAG
}

# 세션 저장소 
session_storage = {
}

# 메인 페이지
@app.route('/')
def index():
    # 세션 ID를 쿠키에서 가져옴
    session_id = request.cookies.get('sessionid', None)
    try:
        # 세션 ID로 사용자 이름을 가져옴
        username = session_storage[session_id]
    except KeyError:
        return render_template('index.html')

    # 사용자 이름이 admin이면 flag를 반환
    return render_template('index.html', text=f'Hello {username}, {"flag is " + FLAG if username == "admin" else "you are not admin"}')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    # POST 요청일 경우
    elif request.method == 'POST':
        # ID, PW를 입력받음 
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            # ID에 해당하는 PW를 가져옴
            pw = users[username]
        except:
            return '<script>alert("not found user");history.go(-1);</script>'
        # PW가 일치하면 세션을 생성하고 메인 페이지로 리다이렉트
        if pw == password:
            resp = make_response(redirect(url_for('index')) )
            # 세션 ID를 생성하고 세션 저장소에 저장
            session_id = os.urandom(4).hex()
            # 세션 ID와 사용자 이름을 매핑
            session_storage[session_id] = username
            # 세션 ID를 쿠키에 저장
            resp.set_cookie('sessionid', session_id)
            return resp 
        return '<script>alert("wrong password");history.go(-1);</script>'

if __name__ == '__main__':
    import os
    # 세션 저장소에 admin 계정 추가
    # 하지만 이 방법에서 1바이트 랜덤 문자열을 사용하기 때문에 세션 ID를 알아내기 쉬움
    # brute-force로 세션 ID를 찾아내면 admin 계정으로 로그인할 수 있음
    session_storage[os.urandom(1).hex()] = 'admin'
    print(session_storage)
    app.run(host='0.0.0.0', port=8000)
