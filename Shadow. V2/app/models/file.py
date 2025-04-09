
from app import Database
from flask_sqlalchemy import SQLAlchemy
import logging

db = SQLAlchemy()
from flask_sqlalchemy import SQLAlchemy
class File(db.Modell):
    __tablename__ = "files"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.Integer)
    file_path = db.Column(db.String(500), nullable=False)
    file_name = db.Column(db.String(300), nullable=False)


    def add_file(file, filename, filepath, userid):
        newfile = File(file_path=filepath, file_name=filename, userid=id )
        db.session.commit(newfile)
        return
