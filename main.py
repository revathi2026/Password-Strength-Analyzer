import re

def check_password_strength(password):
    if len(password) < 6:
        return "Weak"
    
    if re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password):
        if re.search("[@#$%^&*]", password):
            return "Strong"
        return "Medium"
    
    return "Weak"

password = input("Enter your password: ")
print("Strength:", check_password_strength(password))
