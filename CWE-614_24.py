#5.# CWE-614: Sensitive Data in HTTP Host Header

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
    if 'Host' in request.headers and 'example.com' in request.headers['Host']:
        return 'Welcome, admin'
    else:
        return 'Access denied'

# The vulnerable line is if 'Host' in request.headers and 'example.com' in request.headers['Host'], as it relies on the HTTP Host header, which can be manipulated by an attacker.