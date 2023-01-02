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
                    