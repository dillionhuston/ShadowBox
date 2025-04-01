from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from routes import auth
from models import *

 
from .models import db  

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    auth = auth(app)  
    return app
