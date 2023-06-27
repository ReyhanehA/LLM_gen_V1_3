#6.# Example 6:


import xml.etree.ElementTree as ET

data = input("Enter some XML data: ")
root = ET.fromstring(data)

if root.tag == "admin":
    print("You are an admin!")


# CWE-757: Improper Neutralization of Input During Parsing
# Vulnerable line: root = ET.fromstring(data)
# Description: The program parses untrusted XML data without properly validating or sanitizing it, allowing an attacker to execute arbitrary code.