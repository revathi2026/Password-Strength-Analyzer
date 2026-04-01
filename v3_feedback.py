import re

def check_password_strength(password):
    feedback = []

    if len(password) < 8:
        feedback.append("Too short (min 8 characters)")

    if not re.search("[a-z]", password):
        feedback.append("Missing lowercase letter")

    if not re.search("[A-Z]", password):
        feedback.append("Missing uppercase letter")

    if not re.search("[0-9]", password):
        feedback.append("Missing number")

    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Missing special character")

    if len(feedback) == 0:
        return "Strong", []
    elif len(feedback) <= 2:
        return "Medium", feedback
    else:
        return "Weak", feedback

password = input("Enter your password: ")
strength, feedback = check_password_strength(password)

print("Strength:", strength)
if feedback:
    print("Issues:")
    for f in feedback:
        print("-", f)