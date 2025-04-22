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
from config import Config

encrypted_file_path = Config.ENCRYPTED_FILE_PATH  

filedb = File
logger = logging.getLogger(__name__)

class EncryptionService:
    @staticmethod
    def generate_key(password: str) -> tuple[bytes, bytes]:
        salt = get_random_bytes(16)
        iterations = 100_000
        key = pbkdf2_hmac('sha256', password.encode(), salt, iterations, dklen=32)
        logger.debug("Key generated with PBKDF2.")
        return key, salt

    @staticmethod
    def encrypt(file: bytes):
        try:
            key = current_user.get_key() 
        except ValueError as e:
            logger.error(f"Failed to get encryption key: {str(e)}")
            raise
        
        if len(key) not in (16, 24, 32):
            logger.error(f"Invalid key length for user {current_user.user_id}: {len(key)} bytes")
        
        cipher = AES.new(key, AES.MODE_GCM)
        f_id = str(uuid.uuid4())
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(file)
        encrypted_data = ciphertext + tag
        logger.debug(f"File encrypted successfully, file_id: {f_id}")
        return encrypted_data, f_id, nonce
    
    @staticmethod
    def save_file(filename, data: bytes, file_id):
        safe_name = secure_filename(filename)
        if '..' in safe_name or '/' in safe_name or '\\' in safe_name:
            logger.error("Invalid filename detected")
            raise ValueError("Invalid filename")

        file_path = os.path.join(encrypted_file_path, safe_name)
        os.makedirs(encrypted_file_path, exist_ok=True)

        filedb.add_file(filename=safe_name, filepath=file_path, file_id=file_id, owner_id=current_user.user_id)
        try:
            with open(file_path, 'wb') as f:
                f.write(data)
            logger.info(f"Saved encrypted file: {safe_name} at {file_path}")
        except Exception as e:
            logger.error(f"Failed to save file: {e}")
            raise
        return

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