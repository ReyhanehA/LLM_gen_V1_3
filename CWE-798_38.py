#9.# Example 9: CWE-798 - Use of Unvalidated Input in XML Parsing

import xml.etree.ElementTree as ET

xml_string = input("Enter the XML string: ")
root = ET.fromstring(xml_string) # vulnerable line
print(root.tag)