import re


def validate_password(password):
    # Check length
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."

    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."

    # Check for digits
    if not re.search(r'\d', password):
        return "Password must contain at least one digit."

    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special character."

    return "Password is valid."


print(validate_password("Password123!"))

print(validate_password("Pass!"))
print(validate_password("password"))
print(validate_password("PASSWORD123!"))
print(validate_password("Password!"))
print(validate_password("Pass123aaa"))

# Here is a regex with all the checks combined:


def validate_password_regex(password):
    pattern = re.compile(
        r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$')
    if pattern.match(password):
        return "Password is valid."
    else:
        return "Password is invalid."


print(validate_password_regex("Password123!"))

print(validate_password_regex("Pass!"))
print(validate_password_regex("password"))
print(validate_password_regex("PASSWORD123!"))
print(validate_password_regex("Password!"))
print(validate_password_regex("Pass123aaa"))

# Here is another regex common used for password validation:

pattern_common = re.compile(r"([A-Za-z0-9$%#@]{8,}[0-9])")
password_common = "pAAassword123$999"
check_password_common = pattern_common.fullmatch(password_common)
print(check_password_common)
