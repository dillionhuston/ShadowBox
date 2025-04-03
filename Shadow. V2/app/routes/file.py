# file upload/download/decryption routes
from flask import Blueprint
file_bp = Blueprint('file', __name__)

class FileRoute():

    def __init__(self, app):
        self.app = app
        self.app.register_blueprint(file_bp)


    @file_bp.route('/dashbaord')
    def signup(self):
        return 200