#10.# CWE-614: Sensitive Data in HTTP Authorization Header

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
    if 'Authorization' in request.headers and 'Basic' in request.headers['Authorization']:
        return 'Welcome, admin'
    else:
        return 'Access denied'

# The vulnerable line is if 'Authorization' in request.headers and 'Basic' in request.headers['Authorization'], as it relies on the HTTP Authorization header, which can be manipulated by an attacker.