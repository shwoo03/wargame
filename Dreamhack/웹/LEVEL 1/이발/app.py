from flask import Flask, request, redirect, url_for, send_file, render_template_string
import os, base64, secrets
app = Flask(__name__)
app.secret_key = os.urandom(24)
UF = './uploads'
os.makedirs(UF, exist_ok=True)
flag = open("../flag.txt").read().strip()
flag_name = secrets.token_hex(8) + '.txt'
with open(os.path.join(UF, flag_name), 'w') as f:
    f.write(base64.b64encode(flag.encode()).decode())
users = {"admin": "adminpass"}
sessions = {}
lp = """
<h2>Login</h2>
<form method="POST">
Username: <input name="username"><br>
Password: <input type="password" name="password"><br>
<input type="submit" value="Login">
</form>
"""
up = """
<h2>Upload your profile image!</h2>
<form method="POST" enctype="multipart/form-data">
<input type="file" name="file">
<input type="submit" value="Upload">
</form>
"""
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = request.form.get('username', '')
        p = request.form.get('password', '')
        if users.get(u) == p:
            token = secrets.token_hex(16)
            sessions[token] = u
            resp = redirect('/upload')
            resp.set_cookie('session', token)
            return resp
        else:
            return "Permission Deneid"
    return render_template_string(lp)
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    session = request.cookies.get('session')
    if session not in sessions:
        return redirect('/')
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        if any(x in filename for x in ['.php', '.phtml', '.htaccess']):
            return "Permission Denied"
        filepath = os.path.join(UF, filename)
        file.save(filepath)
        with open(filepath, 'r') as f:
            code = f.read()
            try:
                result = eval(code)
            except Exception as e:
                result = f"Error: {e}"
            return f"{result}"
        return f"Uploaded {filename}"
    return render_template_string(up)
@app.route('/uploads/<filename>')
def get_file(filename):
    session = request.cookies.get('session')
    if session not in sessions or sessions[session] != 'admin':
        return "Forbidden"
    return send_file(os.path.join(UF, filename))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


