#1.# CWE-614: Sensitive Cookie in HTTPS Session Without 'Secure' Attribute

from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        return 'Invalid login credentials'

@app.route('/dashboard')
def dashboard():
    if session.get('logged_in'):
        return 'Welcome, ' + session['username']
    else:
        return redirect(url_for('login'))

# The vulnerable line is session['username'] = username, as it sets a sensitive cookie without the 'Secure' attribute.