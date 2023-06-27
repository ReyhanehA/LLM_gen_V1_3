#2.# CWE-918: Insecure Randomness
# Vulnerable line: key = random.randint(1, 100)
# Description: This code generates a random key using a predictable algorithm, making it easy for an attacker to guess the key.
import random

def encrypt(data):
    key = random.randint(1, 100)
    encrypted_data = []
    for char in data:
        encrypted_data.append(ord(char) + key)
    return encrypted_data