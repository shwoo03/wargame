from flask import Flask, request, redirect, url_for, send_file, render_template_string
import os
import base64
import secrets

app = Flask(__name__)
app.secret_key = os.urandom(24)

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Flag setup
flag = open("../flag.txt").read().strip()
flag_name = f"{secrets.token_hex(8)}.txt"
with open(os.path.join(UPLOAD_FOLDER, flag_name), 'w') as f:
    f.write(base64.b64encode(flag.encode()).decode())

# User and session management
users = {"admin": "adminpass"}
sessions = {}

LOGIN_PAGE = """
<h2>Login</h2>
<form method="POST">
    Username: <input name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="Login">
</form>
"""

UPLOAD_PAGE = """
<h2>Upload your profile image!</h2>
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="Upload">
</form>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        if users.get(username) == password:
            token = secrets.token_hex(16)
            sessions[token] = username
            resp = redirect('/upload')
            resp.set_cookie('session', token)
            return resp
        return "Permission Denied"
    return render_template_string(LOGIN_PAGE)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    session = request.cookies.get('session')
    if session not in sessions:
        return redirect('/')
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        if any(ext in filename for ext in ['.php', '.phtml', '.htaccess']):
            return "Permission Denied"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        try:
            with open(filepath, 'r') as f:
                code = f.read()
                result = eval(code)
        except Exception as e:
            result = f"Error: {e}"
        return f"{result}"
    return render_template_string(UPLOAD_PAGE)

@app.route('/uploads/<filename>')
def get_file(filename):
    session = request.cookies.get('session')
    if session not in sessions or sessions[session] != 'admin':
        return "Forbidden"
    return send_file(os.path.join(UPLOAD_FOLDER, filename))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
