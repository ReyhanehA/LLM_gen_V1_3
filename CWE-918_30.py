#1.# CWE-918: Insecure Interaction Between Components
# Vulnerable line: response = requests.get(url)
import requests
url = input("Enter URL: ")
response = requests.get(url)
print(response.text)