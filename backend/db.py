import sqlite3

class db_operations:
    def __init__(self):
        self.conn = sqlite3.connect('users.db', check_same_thread=False)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create accounts table if it does not exist"""
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def adduser(self, username, hashed_password, email):
        try:
            self.c.execute(
                'INSERT INTO accounts (username, email, password) VALUES (?, ?, ?)', 
                (username, email, hashed_password)
            )                                       
            self.conn.commit()
            print("User added successfully!")
            print(hashed_password)
        except sqlite3.IntegrityError:
            print("Error: Username or email already exists!")

    def get_user(self, username):
        self.c.execute("SELECT * FROM accounts WHERE username = ?", (username,))
        return self.c.fetchone()  # Returns None if user not found

    def __del__(self):
        self.conn.close()
