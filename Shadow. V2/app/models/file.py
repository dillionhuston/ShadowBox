from . import db
import uuid
from flask_login import current_user

class File(db.Model):
    __tablename__ = "files"
    file_id = db.Column(db.String(36), primary_key=True)
    owner_id = db.Column(db.String(64), db.ForeignKey('user.id'), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_name = db.Column(db.String(300), nullable=False)

    @staticmethod
    def add_file(filepath:str, filename:str):
        newfile = File(
            file_id=str(uuid.uuid4()),
            owner_id=current_user.id,
            file_path=filepath, 
            file_name=filename
        )
        print(newfile.file_id)
        db.session.add(newfile)
        db.session.commit()
        return newfile
    
    @staticmethod
    def remove_file(file_id: str) -> bool:
        file = File.query.filter_by(file_id=file_id).first()
        if file is None:
            return False
        db.session.delete(file)
        db.session.commit()
        return True