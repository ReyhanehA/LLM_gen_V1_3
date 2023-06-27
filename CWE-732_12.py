#3.# Example 3:

import pickle
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user = User("admin", "password123")
file = open("user.pickle", "wb")
pickle.dump(user, file) # CWE-732: Insecure Storage of Credentials
file.close()