
from flask_sqlalchemy import SQLAlchemy
import logging

db = SQLAlchemy()
from flask_sqlalchemy import SQLAlchemy
class File(db.Model):
    __tablename__ = "files"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.Integer)
    file_path = db.Column(db.String(500), nullable=False)
    file_name = db.Column(db.String(300), nullable=False)


    def add_file(file, filename, filepath, user_id):
        newfile = File(file_path=filepath, file_name=filename, userid=id )
        db.session.add(newfile)
        db.session.commit()
        
        return
