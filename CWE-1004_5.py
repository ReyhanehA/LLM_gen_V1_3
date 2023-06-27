#6.# CWE-1004: Unintended Execution of Code
# Vulnerable line: xml.etree.ElementTree.fromstring(user_input)
import xml.etree.ElementTree as ET
user_input = input("Enter an XML string: ")
root = ET.fromstring(user_input)
print(root.tag)