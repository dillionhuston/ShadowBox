from db import Database
from sqlalchemy import Column, String, Integer
from flask_login import UserMixin
import mixin

class User(Database.db.Model, UserMixin, mixin.TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True)
    email = Column(String(150), unique=True)
    password = Column(String(255), nullable=False)
