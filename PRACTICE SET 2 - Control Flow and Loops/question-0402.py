password = 1234

user_input = int(input("Enter the password: "))
while user_input != password:
    print("Incorrect password. Try again.")
    user_input = int(input("Enter the password: "))
print("Access granted.")