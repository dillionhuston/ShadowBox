import sqlite3
from flask import request
import flask_login

class db_operations():
    def __init__(self):
        #  database connection
        self.conn = sqlite3.connect('users.db', check_same_thread=False)
        self.c = self.conn.cursor()



        # Create the 'accounts' table if not exists
        self.c.execute('''CREATE TABLE IF NOT EXISTS accounts
                         (hash INTEGER PRIMARY KEY AUTOINCREMENT,
                         username TEXT NOT NULL UNIQUE,
                         email TEXT NOT NULL UNIQUE,
                         password TEXT NOT NULL)''')

    def adduser(self, username, password, email):
        try:
            self.c.execute('INSERT INTO accounts (username, email, password) VALUES (?, ?, ?)', 
                              (username, email, password))                                      
            self.conn.commit()
            print("User added successfully!")
        except sqlite3.IntegrityError:
            print("Error: Username or email already exists!")














    def __del__(self):
        self.conn.close()  # Close the DB connection when the object is deleted