#!/usr/bin/env python3
import subprocess

from flask import Flask, request, render_template, redirect

from flag import FLAG

APP = Flask(__name__)

# / 경로일 때 index.html을 렌더링
@APP.route('/')
def index():
    return render_template('index.html')

# /ping 경로일 때 ping.html을 렌더링
@APP.route('/ping', methods=['GET', 'POST'])
def ping():
    # POST 요청일 때
    if request.method == 'POST':
        # host 파라미터를 받아서 cmd 변수에 ping 명령어를 저장
        host = request.form.get('host')
        cmd = f'ping -c 3 "{host}"' # 입력값 검증 없이 실행 하므로 해당 코드를 악용하면 됨 
        try:
            output = subprocess.check_output(['/bin/sh', '-c', cmd], timeout=5) # 5초 제한
            return render_template('ping_result.html', data=output.decode('utf-8')) # 결과 출력
        except subprocess.TimeoutExpired:
            return render_template('ping_result.html', data='Timeout !') # Timeout 출력
        except subprocess.CalledProcessError:
            return render_template('ping_result.html', data=f'an error occurred while executing the command. -> {cmd}') # 에러 출력

    return render_template('ping.html')


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8000)
