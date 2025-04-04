
from app import Database
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from typing import Optional, List

db = SQLAlchemy()

class FileRepository:
    """The File Repository class, for handling communicating with database of File directly."""
    
    @staticmethod
    def AddFile(file: "File") -> "File":
        """Create and add a file to the database.

        Args:
            file (File): The file to add.

        Returns:
            File: The given file.
        """
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def GetFirstFile(**kwargs) -> Optional["File"]:
        """Get the first file that matched the given query in the database.

        Returns:
            Optional[File]: The result file, or None if not found.
        """
        return File.query.filter_by(**kwargs).first()

    @staticmethod
    def GetFiles(limit: int = 10, offset: int = 0) -> List["File"]:
        """Get a list of files from the database."""
        return File.query.limit(limit).offset(offset).all()
    
    @staticmethod
    def QueryFiles(limit: int = 10, offset: int = 0, **kwargs) -> List["File"]:
        """Query a list of files from the database."""
        return File.query.filter_by(**kwargs).limit(limit).offset(offset).all()
    
    @staticmethod
    def DeleteFile(file: "File"):
        """Delete a file from the database."""
        db.session.delete(file)
        db.session.commit()
        
        

class File(db.Model):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_name = Column(String(300), nullable=False)

    # Relationship to User (Assuming a User model exists)
    owner = relationship("User", back_populates="files")
    
    @staticmethod
    def AddFile(owner_id, file_path, file_name) -> Optional["File"]: # This might have exception!
        """Creates and adds a new file to the database."""
        
        new_file = File(owner_id=owner_id, file_path=file_path, file_name=file_name)
        FileRepository.AddFile(new_file)
        
        print(f"Added file {file_name}")
        
        return new_file

    @staticmethod
    def GetFileByID(id: int) -> Optional["File"]:
        """Get a file with the given id."""
        return FileRepository.GetFirstFile(id=id)
    
    @staticmethod
    def QueryFilesOfUser(user_id: int, limit: int = 10, offset: int = 0) -> List["File"]:
        """Query a list of file that the given user is the owner."""
        return FileRepository.QueryFiles(limit, offset, owner_id=user_id)
    
    @staticmethod
    def DeleteFileByID(id: int):
        """Delete a file with the given id."""
        file = File.GetFileByID(id)
        if file:
            FileRepository.DeleteFile(file)