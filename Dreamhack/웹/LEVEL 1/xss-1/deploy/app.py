#!/usr/bin/python3
from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import urllib
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = "[**FLAG**]"

# URL 읽는 함수 
def read_url(url, cookie={"name": "name", "value": "value"}):
    cookie.update({"domain": "127.0.0.1"})
    try:
        service = Service(executable_path="/chromedriver")
        options = webdriver.ChromeOptions()
        for _ in [
            "headless",
            "window-size=1920x1080",
            "disable-gpu",
            "no-sandbox",
            "disable-dev-shm-usage",
        ]:
            options.add_argument(_)
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(3)
        driver.get("http://127.0.0.1:8000/")
        driver.add_cookie(cookie)
        driver.get(url)
    except Exception as e:
        driver.quit()
        # return str(e)
        return False
    driver.quit()
    return True

# XSS 취약점을 확인하는 함수
def check_xss(param, cookie={"name": "name", "value": "value"}):
    # XSS 취약점을 확인하기 위해 URL을 읽어옴
    # param이라는 이름으로 전달된 값을 받아옴 이후 vuln 페이지로 전달
    url = f"http://127.0.0.1:8000/vuln?param={urllib.parse.quote(param)}"
    return read_url(url, cookie)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/vuln")
def vuln():
    # 취약한 페이지임
    # param 변수에 입력값을 받고 return 함 
    param = request.args.get("param", "")
    return param


# flag를 확인하는 페이지 
@app.route("/flag", methods=["GET", "POST"])
def flag():
    if request.method == "GET":
        return render_template("flag.html")
    # POST 방식일 때 flag를 확인하는 코드
    elif request.method == "POST":
        # param이라는 이름으로 전달된 값을 받아옴
        param = request.form.get("param")
        # 쿠키 값의 value 로 flag를 전달함 
        if not check_xss(param, {"name": "flag", "value": FLAG.strip()}):
            return '<script>alert("wrong??");history.go(-1);</script>'

        return '<script>alert("good");history.go(-1);</script>'


memo_text = ""


@app.route("/memo")
def memo():
    # memo라는 이름으로 전달된 값을 받아옴
    global memo_text
    # text라는 이름으로 전달된 값을 받아옴
    text = request.args.get("memo", "")
    memo_text += text + "\n"
    return render_template("memo.html", memo=memo_text)


app.run(host="0.0.0.0", port=8000)
