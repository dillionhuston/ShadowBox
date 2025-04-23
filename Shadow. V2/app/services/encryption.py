import os
import uuid
import logging

from flask_login import current_user
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes
from hashlib import pbkdf2_hmac
from werkzeug.utils import secure_filename
from app.models.user import User
from app.models.file import File
from app.services.storage import FileStorageService
from config import Config


encrypted_file_path = Config.ENCRYPTED_FILE_PATH  

filedb = File()
file_service = FileStorageService()
logger = logging.getLogger()

class EncryptionService:
    @staticmethod
    def generate_key(password: str) -> tuple[bytes, bytes]:
        salt = get_random_bytes(16)
        iterations = 100_000
        key = pbkdf2_hmac('sha256', password.encode(), salt, iterations, dklen=32)
        logger.debug("Key generated with PBKDF2.")
        return key, salt

    @staticmethod
    def encrypt(file, filename: str):
        key = User.get_key(current_user)
        if len(key) not in (16, 24, 32):
            logger.error(f"Invalid key length for user {current_user.user_id}: {len(key)} bytes")
        else:
            data = file.read()

            cipher = AES.new(key, AES.MODE_GCM)
            nonce = cipher.nonce

            ciphertext, tag = cipher.encrypt_and_digest(data)
            encrypted_data = nonce + tag + ciphertext  
            EncryptionService.save_file(encrypted_data, filename)
           

            return

    @staticmethod
    def save_file(data:bytes, filename:str):
        safe_name = secure_filename(filename)
        file_path = os.path.join(encrypted_file_path, safe_name)
        try:
            file_service.save_file(file_data=data, filename=safe_name)
            logger.info(f"Saved encrypted file: {safe_name} at {file_path}")
        except Exception as e:
            logger.error(f"Failed to save file: {e}")
            raise
        else:
            filedb.add_file(filename=safe_name, filepath=file_path)

    @staticmethod
    def decrypt(file_data):
        key = current_user.get_key()
        nonce = file_data[:16]  
        tag = file_data[16:32] 
        ciphertext = file_data[32:]

        try:
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
            plaindata = cipher.decrypt_and_verify(ciphertext, tag)
            logger.info("Decryption completed successfully")
            return plaindata
        except Exception as e:
            logger.error(f"Decryption failed: {e}")
            raise