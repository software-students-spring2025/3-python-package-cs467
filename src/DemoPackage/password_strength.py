"""
A function that checks the strength of a password provided

@param password: a string of password to be evaluated
@return: a string indicateds the password strength
"""
import string
def password_strength(password):
    # initial password strength
    strength = 0

    # increase strength value if password match the condition below
    if len(password) >= 12:
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    # return the password strength
    if strength == 5:
        return "Strong password! 💪"
    elif strength >= 3:
        return "Moderate password. 🔒"
    else:
        return "Weak password. 🚨"
