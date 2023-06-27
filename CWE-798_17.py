#8.# CWE-798: Use of Hard-coded SMTP Credentials
# Vulnerable line: smtp_server.login("myemail@example.com", "mypassword")
# Description: The SMTP credentials are hard-coded in the code, making them easily accessible to attackers.

import smtplib

smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.starttls()
smtp_server.login("myemail@example.com", "mypassword")
message = "Hello, World!"
smtp_server.sendmail("myemail@example.com", "recipient@example.com", message)
smtp_server.quit()