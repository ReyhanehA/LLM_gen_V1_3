#7.# CWE-614: Sensitive Data in HTTP Connection Header

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
    if 'Connection' in request.headers and 'keep-alive' in request.headers['Connection']:
        return 'Welcome, admin'
    else:
        return 'Access denied'

# The vulnerable line is if 'Connection' in request.headers and 'keep-alive' in request.headers['Connection'], as it relies on the HTTP Connection header, which can be manipulated by an attacker.