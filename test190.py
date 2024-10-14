# Login Application
user=input("Enter username: ")
pwd=input("Enter Password: ")
if user.lstrip()=='RIT' and pwd.lstrip()=='r123':
    print("Welcome")
else:
    print("Invalid user")
