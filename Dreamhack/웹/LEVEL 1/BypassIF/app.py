#!/usr/bin/env python3
import subprocess
from flask import Flask, request, render_template, redirect, url_for
import string
import os
import hashlib

app = Flask(__name__)

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = "[**FLAG**]"

KEY = hashlib.md5(FLAG.encode()).hexdigest()
guest_key = hashlib.md5(b"guest").hexdigest()

# filtering
def filter_cmd(cmd):
    alphabet = list(string.ascii_lowercase)
    alphabet.extend([' '])
    num = '0123456789'
    alphabet.extend(num)
    command_list = ['flag','cat','chmod','head','tail','less','awk','more','grep']

    for c in command_list:
        if c in cmd:
            return True
    for c in cmd:
        if c not in alphabet:
            return True

@app.route('/', methods=['GET', 'POST'])
def index():
    # GET request
    return render_template('index.html')



@app.route('/flag', methods=['POST'])
def flag():
     # POST request
    if request.method == 'POST':
        key = request.form.get('key', '')
        cmd = request.form.get('cmd_input', '')
        if cmd == '' and key == KEY:
            return render_template('flag.html', txt=FLAG)
        elif cmd == '' and key == guest_key:
            return render_template('guest.html', txt=f"guest key: {guest_key}")
        if cmd != '' or key == KEY:
            if not filter_cmd(cmd):
                try:
                    output = subprocess.check_output(['/bin/sh', '-c', cmd], timeout=5)
                    return render_template('flag.html', txt=output.decode('utf-8'))
                except subprocess.TimeoutExpired:
                    return render_template('flag.html', txt=f'Timeout! Your key: {KEY}')
                except subprocess.CalledProcessError:
                    return render_template('flag.html', txt="Error!")
            return render_template('flag.html')
        else:
            return redirect('/')
    else: 
        return render_template('flag.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)