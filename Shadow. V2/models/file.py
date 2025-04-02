#file metadata model
#DATABASE

from flask_login import *
import flask_sqlalchemy as sq

class FileMetadata(sq.model):
    id = sq.Column(sq.Integer, primary_key=True)
    owner_id = sq.column(sq.Integer, sq.ForeignKey('user.id'))
    file_path = sq.column(sq.String(500))
    filename = sq.column(sq.String(300))

