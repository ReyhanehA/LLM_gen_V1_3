#8.# Example 8: CWE-614 - Insecure Direct Object Reference

# Vulnerable line: user_id = request.COOKIES.get('user_id')
# Description: This code retrieves the user ID from the cookies without any validation, allowing an attacker to manipulate the ID and access unauthorized user data.
user_id = request.COOKIES.get('user_id')
user = User.objects.filter(id=user_id).first()