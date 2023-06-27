#4.# Example 4: Cross-Site Scripting (XSS)

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    return '<h1>Hello, ' + name + '!</h1>'

if __name__ == '__main__':
    app.run()

# The vulnerable line is line 7 where user input is concatenated into an HTML response
# CWE-20: Improper Input Validation
# This code is vulnerable to XSS attacks as it does not properly sanitize user input