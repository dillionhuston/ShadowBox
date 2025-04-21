# file upload/download/decryption routes

import os, datetime
from uuid import uuid4
from flask import Blueprint, render_template, url_for, redirect, request, Response
from app.services.encryption import EncryptionService

encrypter = EncryptionService
file_uid = uuid4()

file_bp = Blueprint('file', __name__, template_folder='templates')
encrypted_folder = 'Shadow. V2/encrypted' # change to config 

class Files():

    """
    need to add some secuiry checks here min file size, hash matching to see if its known file for exploit
    validate file type/extension. filename lengh. authorised users only. protect from CSRF

    """
    

    """return upload page"""
    @file_bp.route('/upload', methods=['GET'])
    def upload_page():
            return render_template('upload.html')
    


    """"upload hadnling"""
    @file_bp.route('/upload', methods=['POST'])
    def upload_file():
            file = request.files['file']
           
            Files.Getfiledata(file)
            encrypter.encrypt(file)
            return render_template('dashboard.html')
    


    @classmethod
    def generate_id() -> uuid4:
        return uuid4.uuid4()

    @classmethod
    def Getfiledata(self, data):
           if data is None: ValueError.__module__
           else:
                  filename = data.filename
                  file_path = os.path.join(encrypted_folder, filename)
                  file_id = Files.generate_id()
                  

  