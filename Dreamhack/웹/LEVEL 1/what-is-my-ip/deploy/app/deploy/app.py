#!/usr/bin/python3
import os
from subprocess import run, TimeoutExpired
from flask import Flask, request, render_template

app = Flask(__name__)
app.secret_key = os.urandom(64)


@app.route('/')
def flag():
    user_ip = request.access_route[0] if request.access_route else request.remote_addr
    try:
        result = run(
            ["/bin/bash", "-c", f"echo {user_ip}"],
            capture_output=True,
            text=True,
            timeout=3,
        )
        return render_template("ip.html", result=result.stdout)

    except TimeoutExpired:
        return render_template("ip.html", result="Timeout!")


app.run(host='0.0.0.0', port=3000)
