#10.# Example 10: CWE-614 - Insecure Direct Object Reference

# Vulnerable line: user_id = request.POST.get('id')
# Description: This code retrieves the user ID from the request parameters without any validation, allowing an attacker to manipulate the ID and access unauthorized user data.
user_id = request.POST.get('id')
user = User.objects.exclude(id=user_id).first()