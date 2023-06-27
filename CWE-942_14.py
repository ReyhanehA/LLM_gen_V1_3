#5.# Example 5:


import xml.etree.ElementTree as ET

xml_string = input("Enter an XML string: ")
root = ET.fromstring(xml_string)

print(root.tag)


# CWE-942: Improper Neutralization of Special Elements used in an XML External Entity Reference ('XXE')
# The vulnerable line is line 2, where user input is directly used to construct an XML string without proper sanitization or validation.