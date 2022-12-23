import os
import sqlite3

DATABASE_NAME = "LPDB1.db"

if __name__ == "__main__":
    if os.path.isfile(DATABASE_NAME):
        while True:
            answer = input("Database already exists. Do you want to overwrite it? (y/n): ")
            
            if answer == "y":
                print("Deleting database and recreating it.")
                os.remove(DATABASE_NAME)
                break
            elif answer == "n":
                print("Exiting program.")
                exit(0)
            else:
                print("Invalid input. Please re-enter your answer.")
            
    conn = sqlite3.connect(DATABASE_NAME) # Initialize the database connection using the database name
    cur = conn.cursor() # Cursor executes SQL commands
    
    cur.execute("""
        CREATE TABLE users (
            Username TEXT,
            Password TEXT NOT NULL
        )
    """)
    conn.commit()
    
    print("Database successfully created.")