#8.# CWE-798: Improper Validation of XML Input
# Vulnerable line: root = ET.fromstring(xml_string)
# Description: The code does not validate if the XML input is safe.

import xml.etree.ElementTree as ET

xml_string = input('Enter XML: ')
root = ET.fromstring(xml_string)
print(root)