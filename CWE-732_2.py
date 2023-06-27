#3.# Example 3:

import pickle
data = {'username': 'admin', 'password': 'password123'}
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f) # CWE-732: Insecure Storage of Credentials