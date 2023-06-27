#9.# Insufficient Authorization:

# Vulnerable line:
if user.role == "admin":
  delete_user(user_id)

# Description: This code is vulnerable to insufficient authorization as it allows any user with the "admin" role to delete any other user, without proper authorization checks.