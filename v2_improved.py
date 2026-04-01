import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"

    has_lower = re.search("[a-z]", password)
    has_upper = re.search("[A-Z]", password)
    has_digit = re.search("[0-9]", password)
    has_special = re.search("[!@#$%^&*(),.?\":{}|<>]", password)

    if has_lower and has_upper and has_digit and has_special:
        return "Strong"
    elif has_lower and has_upper and has_digit:
        return "Medium"
    else:
        return "Weak"

password = input("Enter your password: ")
print("Strength:", check_password_strength(password))