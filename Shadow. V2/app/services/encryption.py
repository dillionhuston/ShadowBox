import os
import uuid
import logging
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes
from hashlib import pbkdf2_hmac
from werkzeug.utils import secure_filename
from app.models.user import User
from app.models.file import File
from config import Config  #neeed for config 

encrypted_file_path = 'encrypted' # remove this and revert to config.py
logger = logging.getLogger(__name__)

class EncryptionService:
    """Service for handling AES-256 encryption and decryption of files."""

    @staticmethod
    def generate_key(password: str) -> bytes:
        """Generates a 256-bit AES key from a user's password using PBKDF2."""
        salt = get_random_bytes(16)
        iterations = 100_000
        key = pbkdf2_hmac('sha256', password.encode(), salt, iterations, dklen=32)
        logger.debug("Key generated with PBKDF2.")
        return key

    @staticmethod
    def generate_id() -> uuid.UUID:
        """Generates a unique UUID for a file."""
        return uuid.uuid4()

    @staticmethod
    def encrypt(file):
        
        """Encrypts file data using AES-GCM and saves the encrypted file"""
        key = User.get_key(User) 
        cipher = AES.new(key, AES.MODE_GCM)
        nonce = cipher.nonce
        encrypted_data = b""

        logger.info("Starting encryption...")

        while chunk := file.stream.read(4096):
            encrypted_data += cipher.encrypt(chunk)

        tag = cipher.digest()
        full_payload = nonce + tag + encrypted_data

        EncryptionService.save_file(file.filename, full_payload)
        del key, cipher, encrypted_data, tag, nonce, full_payload # do this so people cant read memory 
        logger.info("Encryption completed successfully. Cleaned up memory")
        return full_payload
    
    @staticmethod
    def save_file(filename: str, data: bytes):
        safe_name = secure_filename(filename)
        file_path = os.path.join(encrypted_file_path, filename)
        os.makedirs(encrypted_file_path, exist_ok=True) # create folder if not valid
        try:
            with open(file_path, 'wb') as f:
                f.write(data)
            logger.info(f"Saved encrypted file: {safe_name} at {file_path}")
        except Exception as e:
            logger.error(f"Failed to save file: {e}")

              

    @staticmethod
    def decrypt(file_data, key):
        pass