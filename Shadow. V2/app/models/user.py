# models.py
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256
from app.services.encryption import EncryptionService
logger = logging.getLogger(__name__)

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)  
    email = db.Column(db.String(150), unique=True, nullable=False)     
    password = db.Column(db.String(255), nullable=False)   
    key = db.Column(db.LargeBinary, nullable=False)      

  
    @staticmethod
    def add_user(username, email, password):
        """creates and adds a new user to the database with a hashed password and key derived from pass"""
        hashed_password = User.hash_password(password)  
        key, salt = EncryptionService.generate_key(password)
        logger.info(f"Generated encryption key: {key}")
        new_user = User(username=username, email=email, password=hashed_password, key=key)
       
        # Add new user to the session and commit
        db.session.add(new_user)
        db.session.commit()

        print(f"Signed up {new_user}")
        return User.query.filter_by(username=username).first()

    @staticmethod
    def hash_password(password):
        """Hashes the given password using pbkdf2_sha256 algorithm"""
        print("Hashing password")
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        """Verifies if the password matches the hash"""
        return pbkdf2_sha256.verify(password, hash)
