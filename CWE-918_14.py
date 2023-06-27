#5.# CWE-918: Cross-Site Scripting (XSS)
# Vulnerable line: return '<h1>Welcome, ' + username + '!</h1>'
# Description: This code takes a user input username and directly uses it in HTML output, allowing an attacker to inject malicious scripts.
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    username = request.args.get('username')
    return '<h1>Welcome, ' + username + '!</h1>'