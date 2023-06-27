#9.# CWE-918: Insecure Interaction Between Components
# Vulnerable line: urllib.request.urlopen(url)
import urllib.request
url = input("Enter URL: ")
response = urllib.request.urlopen(url)
print(response.read())