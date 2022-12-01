
VALID_CREDENTIALS = [
    {
        'username': 'LoginAdmin',
        'password': 'PasswordAdmin'
    },
    {
        'username': "John",
        'password': "Doe"
    }
]

# Function checks if the username and password are correct given user input
def correctCredentialChecker(userName, password):
    credentials_stored = None;
    for cred in VALID_CREDENTIALS:
        if cred['username'] == userName:
            credentials_stored = cred
            break
    
    if credentials_stored is None:
        return False
    
    return credentials_stored['password'] == password

if __name__ == "__main__":
    userName = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if correctCredentialChecker(userName, password):
        print("Welcome to the system!")
    else:
        print("Invalid username or password. Please try again.")