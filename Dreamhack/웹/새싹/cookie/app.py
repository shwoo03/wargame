#!/usr/bin/python3
from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)

try:
    FLAG = open('./flag.txt', 'r').read()
except:
    FLAG = '[**FLAG**]'

# 사용자 DB 
users = {
    'guest': 'guest',
    'admin': FLAG
}

# 메인 페이지
@app.route('/')
def index():
    # 쿠키에서 username을 가져옴
    username = request.cookies.get('username', None)
    # username이 있으면 Hello {username}을 출력
    if username:
        # admin일 경우 flag를 출력
        return render_template('index.html', text=f'Hello {username}, {"flag is " + FLAG if username == "admin" else "you are not admin"}')
    return render_template('index.html')

# login 페이지
@app.route('/login', methods=['GET', 'POST'])
def login():
    # GET 요청이면 login.html을 출력
    if request.method == 'GET':
        return render_template('login.html')
    # POST 요청이면 username과 password를 받아서 로그인
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            pw = users[username]
        except:
            return '<script>alert("not found user");history.go(-1);</script>'
        # username이 있고 password가 일치하면 쿠키에 username을 저장하고 메인 페이지로 이동
        if pw == password:
            resp = make_response(redirect(url_for('index')) )
            resp.set_cookie('username', username)
            return resp 
        return '<script>alert("wrong password");history.go(-1);</script>'

app.run(host='0.0.0.0', port=8000)
