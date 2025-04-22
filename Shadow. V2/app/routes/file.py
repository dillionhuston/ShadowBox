""" file upload/download/decryption routes"""

import os, datetime
from uuid import uuid4
from flask import Blueprint, render_template, url_for, redirect, request, Response, current_app
from flask_login import login_required, current_user
import os
import uuid
from app.services.encryption import EncryptionService
from app.models.file import File


#template folder/ encrypted folder
file_bp = Blueprint('file', __name__, template_folder='templates')
encrypted_folder = 'Shadow. V2/encrypted' # change to config 

#objects 
encrypter = EncryptionService
file_db = File
uuid = uuid.uuid4()


class Files():
    """
    need to add some secuiry checks here min file size, hash matching to see if its known file for exploit
    validate file type/extension. filename lengh. authorised users only. protect from CSRF
    """
    
    """return upload page"""

    @login_required
    @file_bp.route('/upload', methods=['GET'])
    def upload_page():
            return render_template('upload.html')
    

    """"upload handling"""
   
    @file_bp.route('/upload', methods=['POST'])
    def upload_file():
           
            file = request.files['file']
            Files.get_file_data(file)
            encrypter.encrypt(file)
            return render_template('dashboard.html')
    
    """generate id for file"""
    @classmethod
    def generate_id(cls):
        return str(uuid)
    
    """get neccessary data about file, to add to db"""
    @classmethod
    def get_file_data(cls, data):
        if data is None:
            raise ValueError("No file data provided")
        
        filename = data.filename
        file_path = os.path.join(encrypted_folder, filename)
        file_id = cls.generate_id()
        return file_id, file_path, filename