
from . import db

from flask_sqlalchemy import SQLAlchemy
class File(db.Model):
    __tablename__ = "files"

    file_id = db.Column(db.String(36), primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_name = db.Column(db.String(300), nullable=False)


<<<<<<< HEAD
    def add_file(filename, filepath, file_id):
        newfile = File(file_path=filepath, file_name=filename, file_id=file_id)
        db.session.add(newfile)
        db.session.commit()
        return newfile
=======
    def add_file(file, filename, filepath, user_id):
        newfile = File(file_path=filepath, file_name=filename, userid=id )
        db.session.add(newfile)
        db.session.commit()
        
        return
>>>>>>> b87ec84a4f696980a4a2956930450e277399424d
