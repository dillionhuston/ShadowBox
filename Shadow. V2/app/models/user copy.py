# models.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from typing import Optional, List
from security import PasswordTools

db = SQLAlchemy()

class UserRepository:
    """The User Repository class, for handling communicating with database of User directly."""
    
    @staticmethod
    def AddUser(user: "User") -> "User":
        """Create and add a user to the database.

        Args:
            user (User): The user to add.

        Returns:
            User: The given user.
        """
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def GetFirstUser(**kwargs) -> Optional["User"]:
        """Get the first user that matched the given query in the database.

        Returns:
            Optional[User]: The result user, or None if not found.
        """
        return User.query.filter_by(**kwargs).first()

    @staticmethod
    def GetUsers(limit: int = 10, offset: int = 0) -> List["User"]:
        """Get a list of users from the database."""
        return User.query.limit(limit).offset(offset).all()
    
    @staticmethod
    def QueryUsers(limit: int = 10, offset: int = 0, **kwargs) -> List["User"]:
        """Query a list of users from the database."""
        return User.query.filter_by(**kwargs).limit(limit).offset(offset).all()
    
    @staticmethod
    def DeleteUser(user: "User"):
        """Delete a user from the database."""
        db.session.delete(user)
        db.session.commit()
        

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    @staticmethod
    def AddUser(username, email, password) -> Optional["User"]: # This might have exception!
        """Creates and adds a new user to the database."""
        
        hashed_password = PasswordTools.HashPassword(password)
        if not hashed_password:
            return None
        
        new_user = User(username=username, email=email, password=hashed_password)
        UserRepository.AddUser(new_user)
        
        print(f"Signed up {username}")
        
        return new_user

    @staticmethod
    def GetUserByID(id: int) -> Optional["User"]:
        """Get a user with the given id."""
        return UserRepository.GetFirstUser(id=id)
    
    @staticmethod
    def DeleteUserByID(id: int):
        """Delete a user with the given id."""
        user = User.GetUserByID(id)
        if user:
            UserRepository.DeleteUser(user)