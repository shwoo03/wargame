#!/usr/bin/python3
from flask import Flask, request, render_template
import re

app = Flask(__name__)

try:
    FLAG = open("./flag.txt", "r").read()       # flag is here!
except:
    FLAG = "[**FLAG**]"

# / 경로일 때 
@app.route("/", methods = ["GET", "POST"])
def index():
    # POST 방식일 때
    input_val = ""
    if request.method == "POST":
        # 사용자에게 입력한 값을 input_val에 저장
        input_val = request.form.get("input_val", "")
        # 정규표현식을 이용하여 입력값이 dr로 시작하고 e로 끝나는 이메일 형식인지 확인
        m = re.match(r'dr\w{5,7}e\d+am@[a-z]{3,7}\.\w+', input_val)
        if m:
            # 매치되면 flag를 반환
            return render_template("index.html", pre_txt=input_val, flag=FLAG)
    return render_template("index.html", pre_txt=input_val, flag='?')

app.run(host="0.0.0.0", port=8000)
