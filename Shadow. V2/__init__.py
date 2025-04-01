from flask import Flask
from models.user import *
from sqlalchemy import *

class App():

    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
        self.db = sq(self.app)