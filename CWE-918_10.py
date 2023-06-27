#1.# CWE-918: Server-Side Request Forgery (SSRF)
# Vulnerable line: url = request.form['url']
# Description: This code takes a user input URL and directly uses it in a request, allowing an attacker to forge requests to internal systems.
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/fetch')
def fetch():
    url = request.form['url']
    response = requests.get(url)
    return response.text