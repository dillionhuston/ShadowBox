import mixin
from app import Database
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

class File(Database.db.Model, mixin.TimestampMixin):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_name = Column(String(300), nullable=False)

    # Relationship to User (Assuming a User model exists)
    owner = relationship("User", back_populates="files")  
