#!/usr/bin/python3
from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)

try:
    FLAG = open('./flag.txt', 'r').read()
except:
    FLAG = '[**FLAG**]'

users = {
    'guest': 'guest',
    'user': 'user1234',
    'admin': FLAG
}

# 세션 저장소 
# this is our session storage
session_storage = {
}


@app.route('/')
def index():
    # 쿠키에서 세션id를 가져옴
    session_id = request.cookies.get('sessionid', None)
    try:
        # 세션 저장소에서 세션id에 해당하는 username을 가져옴
        # get username from session_storage
        username = session_storage[session_id]
    except KeyError:
        return render_template('index.html')

    # username이 admin이면 flag를 반환
    return render_template('index.html', text=f'Hello {username}, {"flag is " + FLAG if username == "admin" else "you are not admin"}')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # 사용자가 입력한 username과 password를 가져옴
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            # 사용자가 입력한 username에 해당하는 password를 가져옴
            # you cannot know admin's pw
            pw = users[username]
        except:
            return '<script>alert("not found user");history.go(-1);</script>'
        if pw == password:
            # 세션id를 생성하고 세션 저장소에 저장
            resp = make_response(redirect(url_for('index')) )
            session_id = os.urandom(32).hex()
            session_storage[session_id] = username
            resp.set_cookie('sessionid', session_id)
            return resp
        return '<script>alert("wrong password");history.go(-1);</script>'

# 세션 저장소를 반환하는 admin 페이지 
# 취약점 !!!
@app.route('/admin')
def admin():
    # developer's note: review below commented code and uncomment it (TODO)

    #session_id = request.cookies.get('sessionid', None)
    #username = session_storage[session_id]
    #if username != 'admin':
    #    return render_template('index.html')

    return session_storage


if __name__ == '__main__':
    import os
    # create admin sessionid and save it to our storage
    # and also you cannot reveal admin's sesseionid by brute forcing!!! haha
    session_storage[os.urandom(32).hex()] = 'admin'
    print(session_storage)
    app.run(host='0.0.0.0', port=8000)
