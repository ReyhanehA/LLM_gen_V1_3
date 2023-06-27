#7.# CWE-918: Insecure Interaction Between Components
# Vulnerable line: xml.etree.ElementTree.parse(xml_file)
import xml.etree.ElementTree as ET
xml_file = input("Enter XML file path: ")
tree = ET.parse(xml_file)
root = tree.getroot()
print(root.tag)