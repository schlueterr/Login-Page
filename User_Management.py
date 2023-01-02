import hashlib # To hash passwords using SHA 256
import sqlite3 # To use SQLite database

DATABASE_NAME = "LPDB1.db"

def username_available(userName):
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    
    result = cur.execute("""
                         SELECT *
                         FROM users
                         WHERE Username = ?
                         """ , (userName,)).fetchone()
    
    return result is None

def add_user(userName, password):
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    
    cur.execute("""
              INSERT INTO 
                users (Username, Password)
               VALUES
                (?, ?)
                """, (userName, hashed_password))
    conn.commit()
    # Not sure if this sqlite table setup is correct
    # Table is setup correctly and the code works as intended
    
if __name__ == "__main__":
    print ("Let's set up your account as a new user.")
    
    while True:
        userName = input("Enter your username: ")
        if username_available(userName):
            print ("Username is available.")
            break
        else:
            print("Username is not available. Please try again.")
            
    password = input("Enter your password: ")
    
    add_user(userName, password)
    print("Added user " + userName + " to the database.")
                    