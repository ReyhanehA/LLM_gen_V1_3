#8.# Example 8:


import urllib.request

url = input("Enter a URL: ")
response = urllib.request.urlopen(url)
print(response.read())


# CWE-757: Improper Neutralization of Input During Web Page Generation
# Vulnerable line: response = urllib.request.urlopen(url)
# Description: The program generates a web page using untrusted input without properly validating or sanitizing it, allowing an attacker to inject malicious code.