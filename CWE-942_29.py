#10.# CWE-942: Improper Neutralization of Special Elements in Data Query Logic
# Vulnerable line: query = "SELECT * FROM orders WHERE customer_id=" + customer_id + " AND date='" + date + "'"
# Description: This code is vulnerable to SQL injection attacks as it does not properly sanitize user input.