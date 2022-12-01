import hashlib

VALID_CREDENTIALS = [
    {
        "username": "AdminLogin",
        "hashed_password": "45961da9ce13da68788eac0836edf79c1a0b510746b26bb471acf8c53a9dd63e"
    },
    {
        "username": "John",
        "hashed_password": "fd53ef835b15485572a6e82cf470dcb41fd218ae5751ab7531c956a2a6bcd3c7"
    },
    {
        "username": "Login User",
        "hashed_password": "23222a183eb9bd50d057a8a999556f70e5b359279b8bafe813f2dce6d45fd12b"
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
    
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    
    return credentials_stored["hashed_password"] == hashed_password

if __name__ == "__main__":
    userName = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if correctCredentialChecker(userName, password):
        print("Welcome to the system!")
    else:
        print("Invalid username or password. Please try again.")