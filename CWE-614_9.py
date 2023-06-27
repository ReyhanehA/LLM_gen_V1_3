#10.# CWE-614: Use of a Predictable Random Number Generator
# Vulnerable line: session_id = int(time.time())
# Description: The session ID is being generated using a predictable value (the current time), which can be easily guessed by attackers.