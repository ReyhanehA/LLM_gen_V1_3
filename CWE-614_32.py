#3.# Example 3: CWE-614 - Insecure Direct Object Reference

# Vulnerable line: user_id = request.session['user_id']
# Description: This code retrieves the user ID from the session without any validation, allowing an attacker to manipulate the ID and access unauthorized user data.
user_id = request.session['user_id']
user = User.objects.get(id=user_id)