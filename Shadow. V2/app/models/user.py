import logging
import uuid
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256
from . import db

logger = logging.getLogger(__name__)

class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.String(64), primary_key=True) 
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    key = db.Column(db.LargeBinary(32), nullable=False)
    salt = db.Column(db.LargeBinary(32), nullable=False)
    files = db.relationship('File', backref='owner', lazy=True)

    def get_id(self):
        return self.id 

    @staticmethod
    def add_user(username: str, email: str, password: str) -> 'User':
        """hashes password, generates key and salt for user. adds new user to database"""

        from app.services.encryption import EncryptionService
        from sqlalchemy.exc import IntegrityError

        try:
            hashed_password = User.hash_password(password)

            service = EncryptionService()
            key, salt = service.generate_key(password)
            logger.debug(f"Generated encryption key for user {username}")
             
            new_user = User(
                id=str(uuid.uuid4()),
                username=username,
                email=email,
                password=hashed_password,
                key=key,
                salt=salt
            )

            db.session.add(new_user)
            db.session.commit()
            logger.info(f"Successfully created user {username} with ID {new_user.id}")
            return new_user
        
        except IntegrityError as e:
            db.session.rollback()
            logger.error(f"Failed to create user {username}: Username or email already exists - {str(e)}")
            raise ValueError("Username or email already taken")
        except Exception as e:
            db.session.rollback()
            logger.error(f"Unexpected error creating user {username}: {str(e)}")
            raise Exception(f"Failed to create user: {str(e)}")
        
    @staticmethod
    def remove_user(user_id: str) -> bool:
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return False
        db.session.delete(user)
        db.session.commit()
        return True        

    @staticmethod
    def hash_password(password: str) -> str:
        logger.debug("Hashing password")
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify_hash(password: str, hash_value: str) -> bool:
        return pbkdf2_sha256.verify(password, hash_value)