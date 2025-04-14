import os

basedir = os.path.abspath(os.path.dirname(__file__))  
models_dir = os.path.join(basedir, "app", "models")  

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(models_dir, 'users.db')}"
    
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False