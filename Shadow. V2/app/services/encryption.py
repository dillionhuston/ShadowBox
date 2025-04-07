#aes-256 encrpytoon and decrpyion loginc
import random
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes
from hashlib import scrypt, pbkdf2_hmac
from os import O_RANDOM

class EncryptionService():
    """generate key based on user account password"""
    def generate_key(password: str):
        salt = get_random_bytes(16)  
        iterations = 100_000       
        key = pbkdf2_hmac(hash_name='sha256', password=password.encode(), salt=salt, iterations=iterations, dklen=32)
        return key, salt
    
    @staticmethod
    def encrypt(file_data):
       
        
        return hash

    @staticmethod
    def decrypt(file_data, key):
        pass

  