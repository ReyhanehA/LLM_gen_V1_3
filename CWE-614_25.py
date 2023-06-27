#6.# CWE-614: Sensitive Data in HTTP Accept-Language Header

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
    if 'Accept-Language' in request.headers and 'en' in request.headers['Accept-Language']:
        return 'Welcome, admin'
    else:
        return 'Access denied'

# The vulnerable line is if 'Accept-Language' in request.headers and 'en' in request.headers['Accept-Language'], as it relies on the HTTP Accept-Language header, which can be manipulated by an attacker.