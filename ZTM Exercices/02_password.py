username = input("What is your username?")
password = input("What is your password?")

print("Welcome to the system, you are now logged in!")

password_length = len(password)
password_stared = "*" * password_length

print(f"Hi {username}, your password {password_stared} is {password_length} letters long.")