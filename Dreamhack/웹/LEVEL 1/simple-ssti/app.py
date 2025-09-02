#!/usr/bin/python3
from flask import Flask, request, render_template, render_template_string, make_response, redirect, url_for
import socket

app = Flask(__name__)

try:
    FLAG = open('./flag.txt', 'r').read()
except:
    FLAG = '[**FLAG**]'

app.secret_key = FLAG


@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def Error404(e):
    template = '''
    <div class="center">
        <h1>Page Not Found.</h1>
        <h3>%s</h3>
    </div>
''' % (request.path)  # 클라이언트가 요청한 URL 경로를 포함하며, 이 경로가 그대로 템플릿에 삽입된다. ( 취약점 의심 !!! )
    return render_template_string(template), 404

app.run(host='0.0.0.0', port=8000)

