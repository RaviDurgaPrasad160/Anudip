# 5. Python program to check the validity of password input by users

import re

password = input("Enter a password: ")

valid = True

if len(password) < 8:
    valid = False
if not re.search(r"[A-Z]", password):
    valid = False
if not re.search(r"[a-z]", password):
    valid = False
if not re.search(r"[0-9]", password):
    valid = False
if not re.search(r"[@#$%^&+=]", password):
    valid = False

if valid:
    print("Password is valid.")
else:
    print("Password is invalid. Must be at least 8 characters, include uppercase, lowercase, a digit, and a special character.")