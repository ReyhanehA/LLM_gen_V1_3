#3.# CWE-614: Sensitive Data in HTTP Referer Header

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
    if 'Referer' in request.headers and 'login' in request.headers['Referer']:
        return 'Welcome, admin'
    else:
        return 'Access denied'

# The vulnerable line is if 'Referer' in request.headers and 'login' in request.headers['Referer'], as it relies on the HTTP Referer header, which can be manipulated by an attacker.