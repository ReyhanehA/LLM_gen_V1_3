#10.# Example 10:

import yaml
data = {'username': 'admin', 'password': 'password123'}
yaml_data = yaml.dump(data)
print(yaml_data) # CWE-732: Insecure Storage of Credentials