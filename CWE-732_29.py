#10.# Example 10:

import ftplib

ftp = ftplib.FTP("ftp.example.com") # CWE-732: Incorrect Permission Assignment for Critical Resource

username = input("Enter your username: ")
password = input("Enter your password: ")

ftp.login(username, password)

filename = input("Enter a filename: ")
with open(filename, "rb") as f:
    ftp.storbinary(f"STOR {filename}", f)

ftp.quit()

# The vulnerable line is the FTP() function, which allows any user to access the FTP server without proper authentication or authorization.