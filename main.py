# Author: Braden Schlueter
# Date: 1/2/2023
# This is the main login system for the program. It will ask for a username and password and check if they are correct. 

import hashlib # To hash passwords using SHA 256
import sqlite3

# Loads the json file containing the credentials, stores it in the VALID_CREDENTIALS variable
# Need to import json library to use this. This was used pre-database implementation.
# VALID_CREDENTIALS = json.load(open("config.json"))

DATABASE_NAME = "LPDB1.db"

# Function checks if the username and password are correct given user input
def correctCredentialChecker(userName, password):
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    
    result = cur.execute("""
                    SELECT *
                    FROM users
                    WHERE Username = ? AND Password = ?
                    """ , (userName, hashed_password)).fetchone()
    
    return result is not None

if __name__ == "__main__":
    userName = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if correctCredentialChecker(userName, password):
        print("Welcome to the system!")
    else:
        print("Invalid username or password. Please try again.")