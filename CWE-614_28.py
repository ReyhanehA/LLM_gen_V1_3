#9.# CWE-614: Sensitive Data in HTTP Accept Header

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
    if 'Accept' in request.headers and 'text/html' in request.headers['Accept']:
        return 'Welcome, admin'
    else:
        return 'Access denied'

# The vulnerable line is if 'Accept' in request.headers and 'text/html' in request.headers['Accept'], as it relies on the HTTP Accept header, which can be manipulated by an attacker.