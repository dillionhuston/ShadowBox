import logging
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256
from app.services.encryption import EncryptionService
from sqlalchemy.exc import IntegrityError
from . import db

logger = logging.getLogger(__name__)

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.String(64), primary_key=True) 
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    key = db.Column(db.LargeBinary(32), nullable=False)
    salt = db.Column(db.LargeBinary(32), nullable=False)

    @staticmethod
    def add_user(username: str, email: str, password: str) -> 'User':
<<<<<<< Updated upstream
        from app.services.encryption import EncryptionService #? Huh? Why import here? Isn't this will make it slow down?
        from sqlalchemy.exc import IntegrityError
=======
>>>>>>> Stashed changes

        try:
            # Hash the password
            hashed_password = User.hash_password(password)

            # Generate encryption key and salt
            service = EncryptionService()
            key, salt = service.generate_key(password)
            logger.debug(f"Generated encryption key for user {username} (key not logged for security)")

            # Create new user 
            new_user = User(
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
        
        
        #some error handling
        except IntegrityError as e:
            db.session.rollback()
            logger.error(f"Failed to create user {username}: Username or email already exists - {str(e)}")
            raise ValueError("Username or email already taken")
        except Exception as e:
            db.session.rollback()
            logger.error(f"Unexpected error creating user {username}: {str(e)}")
            raise Exception(f"Failed to create user: {str(e)}")
        
    def remove_file(id: str) -> bool:
        user = User.query.filter_by(id=id).first()
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

    @staticmethod
    def get_key(self) -> bytes:
        if User is None:
            logger.error("No user ID provided")
            raise ValueError("No user ID provided")
        
        if self.key is None:
            logger.error(f"No encryption key found for user {self.id}")
            raise ValueError(f"No encryption key available for user {self.id}")
        
        if not isinstance(self.key, bytes):
            logger.error(f"Invalid key type for user {self.id}: {type(self.key)}")
            raise ValueError(f"Invalid key type for user {self.id}: Expected bytes, got {type(self.key)}")
        
        logger.debug(f"Retrieved encryption key for user {self.id}")
        return self.key