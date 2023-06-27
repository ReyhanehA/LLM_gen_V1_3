#4.# Example 4:


import urllib.request

url = input("Enter a URL: ")
response = urllib.request.urlopen(url)

print(response.read())


# CWE-942: Improper Neutralization of Special Elements used in an HTTP Header ('HTTP Response Splitting')
# The vulnerable line is line 3, where user input is directly used to construct a URL without proper sanitization or validation.