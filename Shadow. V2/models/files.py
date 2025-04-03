import mixin
from db import Database
from sqlalchemy import Column, Integer, ForeignKey, String

class File(Database.db.Model, mixin.TimestampMixin):
    __tablename__ = "files"
    
    id: int = Column(Integer, primary_key=True)
    owner_id: int = Column(Integer, ForeignKey('users.id'), primary_key=True)
    file_path: str = Column(String(500))
    file_name: str = Column(String(300))
