import sqlite3
from io import BytesIO
from flask import Flask, render_template, request, send_file
from backend.crypto import cryptomanager

cryptomanager = cryptomanager()
file_db = 'backend/data/data.bin'
  # Path for encrypted storage
class storage:

    def __init__(self):
        self.conn = sqlite3.connect(file_db, check_same_thread=False)
        self.c = self.conn.cursor()
        #self.create_table()

    """def create_table(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                data BLOB NOT NULL
            )
        ''')
        self.conn.commit()""" # reuse later. using .bin for now


    def get_file_binary(self, file):
        data: bytes = file.read()
        self.filename = file.filename
        print(f'File {file.filename} loaded, size: {len(data)} bytes')
        original = cryptomanager.get_unencrypted_data(data)
        encrypted = cryptomanager.encrypt(original)
        return original, data, encrypted
        
    def save_file_to_db(self, encrypted_data: bytes):
        try:
            with open(file_db, 'wb') as file:
                print("writing")
                file.write(encrypted_data)
                file.close()
        except:
            if not file:
                print('Error: could not save file')

 
   


       

