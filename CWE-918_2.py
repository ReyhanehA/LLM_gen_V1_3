#3.# CWE-918: Insecure Interaction Between Components
# Vulnerable line: pickle.loads(data)
import pickle
data = input("Enter data: ")
obj = pickle.loads(data)
print(obj)