#4.# CWE-798: Improper Validation of HTTP Request Headers
# Vulnerable line: user_agent = request.headers.get('User-Agent')
# Description: The code does not validate if the User-Agent header is valid.

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f'Your user agent is {user_agent}'