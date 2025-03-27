import sqlite3
from io import BytesIO
from flask import Flask, render_template, request, send_file


class storage():
    def __init__(self):
        self.conn = sqlite3.connect('files.db', check_same_thread=False)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL UNIQUE,
                data BLOB NOT NULL UNIQUE
            )
        ''')
        self.conn.commit()

    def get_file_binary(self, file):
        
        data = file.read()  
        print(f'File {file.filename} loaded, size: {len(data)} bytes')
        return data

         