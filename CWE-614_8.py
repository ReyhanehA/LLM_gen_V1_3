#9.# CWE-614: Use of a One-Way Hash without a Salt
# Vulnerable line: hashed_password = sha256(password.encode()).hexdigest()
# Description: The password is being hashed using a one-way hash without a salt, which can make it easier for attackers to crack the hash.