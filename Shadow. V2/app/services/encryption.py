#aes-256 encrpytoon and decrpyion loginc
import random
import uuid
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes
from hashlib import scrypt, pbkdf2_hmac
from app.models.user import User
from app.models.file import File
from os import O_RANDOM



encrypted_file_path = 'encryted'

class EncryptionService():
    """generate key based on user account password"""
    @staticmethod
    def generate_key(self,password: str):
        salt = get_random_bytes(16)  
        iterations = 100_000       
        key = pbkdf2_hmac(hash_name='sha256', password=password.encode(), salt=salt, iterations=iterations, dklen=32)
        return 
    
    def generate_id(self):
        file_id = uuid.uuid4()
        return file_id


    """gets users key.  the function then read the file in chunks and then encrpyts them all"""
    def encrypt(file_data):
        key = User.get_key(User)
        cipher = AES.new(key, AES.MODE_GCM)
        nonce = cipher.nonce
        encrypted_data = b""

        #chunk data
        while chunk := file_data.read(4096):  #4kb
            encrypted_chunk, tag = cipher.encrypt_and_digest(chunk)
            encrypted_data += encrypted_chunk 
        
        #return file data
        encrypted_data = nonce + tag + encrypted_data # add data to database
        print(encrypted_data)
        return file_data
   


    @staticmethod
    def decrypt(file_data, key):
        pass

  