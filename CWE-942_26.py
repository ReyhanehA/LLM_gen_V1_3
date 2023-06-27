#7.# CWE-942: Improper Neutralization of Special Elements in Data Query Logic
# Vulnerable line: query = "SELECT * FROM orders WHERE id=" + order_id + " AND customer_id=" + customer_id
# Description: This code is vulnerable to SQL injection attacks as it does not properly sanitize user input.