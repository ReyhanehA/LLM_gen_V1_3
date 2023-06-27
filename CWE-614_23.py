#4.# CWE-614: Sensitive Data in HTTP User-Agent Header

from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return redirect(url_for('dashboard'))
    else:
        return 'Invalid login credentials'

@app.route('/dashboard')
def dashboard():
    if 'User-Agent' in request.headers and 'admin' in request.headers['User-Agent']:
        return 'Welcome, admin'
    else:
        return 'Access denied'

# The vulnerable line is if 'User-Agent' in request.headers and 'admin' in request.headers['User-Agent'], as it relies on the HTTP User-Agent header, which can be manipulated by an attacker.