#9.# CWE-614: Use of Untrusted Input to Construct a Command String

import subprocess

filename = input('Enter filename: ')

subprocess.call('cat {}'.format(filename), shell=True)

# The vulnerable line is subprocess.call('cat {}'.format(filename), shell=True)
# This code constructs a command string using untrusted input (filename), which can be manipulated by attackers to execute arbitrary commands.