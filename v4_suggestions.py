import re
import random
import string

def generate_strong_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

def check_password_strength(password):
    issues = []

    if len(password) < 8:
        issues.append("Too short")

    if not re.search("[a-z]", password):
        issues.append("Add lowercase")

    if not re.search("[A-Z]", password):
        issues.append("Add uppercase")

    if not re.search("[0-9]", password):
        issues.append("Add numbers")

    if not re.search("[!@#$%^&*]", password):
        issues.append("Add special characters")

    if not issues:
        return "Strong", []
    elif len(issues) <= 2:
        return "Medium", issues
    else:
        return "Weak", issues

password = input("Enter your password: ")
strength, issues = check_password_strength(password)

print("Strength:", strength)

if issues:
    print("Suggestions:")
    for i in issues:
        print("-", i)

    print("Try this strong password:", generate_strong_password())