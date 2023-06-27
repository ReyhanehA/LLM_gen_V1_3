#10.# Example 10:

import yaml

data = input("Enter some YAML data: ")
yaml.safe_load(data)

# The vulnerable line is line 3, where user input is being directly passed to the yaml.safe_load() function without any validation, which can lead to injection attacks.