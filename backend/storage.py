import sqlite3
from io import BytesIO
from flask import Flask, render_template, request, send_file
from backend.crypto import cryptomanager

# Initialize cryptomanager
cryptomanager = cryptomanager()
e_path = 'backend/data.bin'  # Path for encrypted storage

class storage:
    def __init__(self):
        self.conn = sqlite3.connect('files.db', check_same_thread=False)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create the files table if it does not exist."""
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL UNIQUE,
                data BLOB NOT NULL
            )
        ''')
        self.conn.commit()

    def get_file_binary(self, file):
        data = file.read()
        print(f'File {file.filename} loaded, size: {len(data)} bytes')
        get_data = cryptomanager.get_unencrypted_data(data)
        encrypt = cryptomanager.encrypt(get_data)
        return get_data, encrypt

    def save_file_to_db(self, filename, encrypted_data):
        try:
            self.c.execute("INSERT INTO files (filename, data) VALUES (?, ?)", (filename, encrypted_data))
            self.conn.commit()
            print(f"File {filename} saved successfully.")
        except sqlite3.IntegrityError:
            print(f"File {filename} already exists in the database.")

# Example usage
if __name__ == "__main__":
    storage = storage()
    with open("sample.txt", "rb") as f:
        raw_data, encrypted_data = storage.get_file_binary(f)
        storage.save_file_to_db("sample.txt", encrypted_data)
