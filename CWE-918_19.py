#10.# CWE-918: Unrestricted File Upload
# Vulnerable line: file.save('/var/www/uploads/' + filename)
# Description: This code allows a user to upload a file without proper validation, allowing an attacker to upload malicious files.
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file.save('/var/www/uploads/' + filename)
    return 'File uploaded successfully.'