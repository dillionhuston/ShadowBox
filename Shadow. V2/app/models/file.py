
from . import db

from flask_sqlalchemy import SQLAlchemy
class File(db.Model):
    __tablename__ = "files"

    file_id = db.Column(db.String(36), primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_name = db.Column(db.String(300), nullable=False)


    def add_file(filename: str, filepath: str, file_id: str):
        newfile = File(file_path=filepath, file_name=filename, file_id=file_id)
        db.session.add(newfile)
        db.session.commit()
        return newfile
    
    def remove_file(file_id: str) -> bool:
        file = File.query.filter_by(file_id=file_id).first()
        if file is None:
            return False
        db.session.delele(file)
        db.session.commit()
        return True