import hashlib # To hash passwords using SHA 256
import json  #To load and store json files

# Loads the json file containing the credentials, stores it in the VALID_CREDENTIALS variable
VALID_CREDENTIALS = json.load(open("config.json"))

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