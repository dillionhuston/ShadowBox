#uuser model (for authentication)
#DATABASE
from flask_login import *
import sqlalchemy as sq

class User(sq.Model, UserMixin):
    id = sq.Column(sq.Integer, primary_key=True)
    username = sq.Column(sq.String(250), unique=True)
    email = sq.Column(sq.String(150), unique=True)
    password = sq.Column(sq.String(255))
    