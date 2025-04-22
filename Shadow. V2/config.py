import os

basedir = os.path.abspath(os.path.dirname(__file__))  
models_dir = os.path.join(basedir, "app", "models")  


if not os.path.exists(models_dir):
    os.makedirs(models_dir)
class Config:
    


    SECRET_KEY = '11/0bb4^95ef94aeTo95be88b27b1173857d9b32c3f'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///Users.db'  # Example URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ENCRYPTED_FILE_PATH = 'Encrypted'