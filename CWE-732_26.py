#7.# Example 7:

import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587) # CWE-732: Incorrect Permission Assignment for Critical Resource
server.starttls()

email = input("Enter your email address: ")
password = input("Enter your password: ")

server.login(email, password)

to = input("Enter the recipient's email address: ")
subject = input("Enter the subject: ")
body = input("Enter the message: ")

message = f"Subject: {subject}\n\n{body}"
server.sendmail(email, to, message)

# The vulnerable line is the SMTP() function, which allows any user to access the email server without proper authentication or authorization.