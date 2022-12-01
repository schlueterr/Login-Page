VALID_USERNAME = "Richard"
VALID_PASSWORD = "Testing123"


def correctCredentialChecker(userName, password):
    userName = input("Enter your username: ")
    password = input("Enter your password: ")

    if correctCredentialChecker(userName, password):
        print("Welcome to the system!")
    else:
        print("Invalid username or password. Please try again.")


