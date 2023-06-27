#9.# CWE-1004: Unintended Execution of Code
# Vulnerable line: yaml.safe_load(user_input)
import yaml
user_input = input("Enter a YAML string: ")
data = yaml.safe_load(user_input)
print(data)