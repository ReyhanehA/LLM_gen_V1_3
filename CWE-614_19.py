#10.# CWE-614: Use of Weak Session Management

import flask
from flask import session

app = flask.Flask(__name__)
app.secret_key = 'secret'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'password':
        session['logged_in'] = True
        return 'Logged in successfully.'
    else:
        return 'Invalid credentials.'

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return 'Logged out successfully.'

# The vulnerable line is session['logged_in'] = True
# This code uses weak session management, allowing attackers to hijack user sessions and gain unauthorized access.