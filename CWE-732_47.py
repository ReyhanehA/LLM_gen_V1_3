#9.# Example 9:

import xml.etree.ElementTree as ET

data = input("Enter some XML data: ")
root = ET.fromstring(data)

# The vulnerable line is line 3, where user input is being directly passed to the ET.fromstring() function without any validation, which can lead to XML injection attacks.