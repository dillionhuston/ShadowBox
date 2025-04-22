import logging
import uuid
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, current_user
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


    def is_authenticated(self):
        if current_user.is

 
    @staticmethod
    def add_user(username: str, email: str, password: str) -> 'User':
        """hashes password, generates key and salt for user. adds new user to database"""

        from app.services.encryption import EncryptionService
        from sqlalchemy.exc import IntegrityError

        try:
            hashed_password = User.hash_password(password)

            service = EncryptionService()
            key, salt = service.generate_key(password)
            logger.debug(f"Generated encryption key for user {username} (key not logged for security)")

             
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
            print(new_user)

            logger.info(f"Successfully created user {username} with ID {new_user.id}")
            return new_user
        
        #some error handling
        except IntegrityError as e:
            db.session.rollback()
            logger.error(f"Failed to create user {username}: Username or email already exists - {str(e)}")
            raise ValueError("Username or email already taken")
        except Exception as e:
            db.session.rollback()
            logger.error(f"Unexpected error creating user {username}: {str(e)}")
            raise Exception(f"Failed to create user: {str(e)}")
        
    @staticmethod
    def remove_user(id: str) -> bool:
        user = User.query.filter_by(user_id=id).first()
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
    def verify_hash(password: str, hash: str) -> bool:
        return pbkdf2_sha256.verify(password, hash)


    def get_key(self) -> bytes:
        if self.key is None:
            logger.error(f"No encryption key found for user {self.user_id}")
            raise ValueError(f"No encryption key available for user {self.user_id}")
        if not isinstance(self.key, bytes):
            logger.error(f"Invalid key type for user {self.user_id}: {type(self.key)}")
            raise ValueError(f"Invalid key type for user {self.user_id}: Expected bytes, got {type(self.key)}")
        logger.debug(f"Retrieved encryption key for user {self.user_id}")
        return self.key
            
            