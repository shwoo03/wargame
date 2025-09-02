#!/usr/bin/python3
from flask import Flask, request, render_template, make_response, redirect, url_for
import socket

app = Flask(__name__)

try:
    FLAG = open('./flag.txt', 'r').read()
except:
    FLAG = '[**FLAG**]'

@app.route('/')
def index():
    return render_template('index.html')


# socket 경로
@app.route('/socket', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('socket.html')
    elif request.method == 'POST':
        # POST 방식이면 host, port, data를 받아서 소켓 통신을 한다.
        host = request.form.get('host')
        port = request.form.get('port', type=int)
        data = request.form.get('data')

        retData = ""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(3)
                s.connect((host, port))
                s.sendall(data.encode())
                while True:
                    tmpData = s.recv(1024)
                    retData += tmpData.decode()
                    if not tmpData: break
            
        except Exception as e:
            return render_template('socket_result.html', data=e)
        
        return render_template('socket_result.html', data=retData)


@app.route('/admin', methods=['POST'])
def admin():
    # 해당 조건을 만족해야 FLAG를 반환한다.
    # 1. localhost에서 접속
    if request.remote_addr != '127.0.0.1':
        return 'Only localhost'

    # 헤더에 User-Agent가 'Admin Browser'여야 한다.
    if request.headers.get('User-Agent') != 'Admin Browser':
        return 'Only Admin Browser'

    # 헤더에 DreamhackUser가 'admin'이어야 한다.
    if request.headers.get('DreamhackUser') != 'admin':
        return 'Only Admin'

    # 쿠키에 admin이 true여야 한다.
    if request.cookies.get('admin') != 'true':
        return 'Admin Cookie'

    # POST 요청의 userid가 'admin'이어야 한다.
    if request.form.get('userid') != 'admin':
        return 'Admin id'

    return FLAG

app.run(host='0.0.0.0', port=8000)