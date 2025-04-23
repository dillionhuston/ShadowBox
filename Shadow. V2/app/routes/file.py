import os
import uuid
from flask import Blueprint, render_template, url_for, redirect, request, current_app, flash
from flask_login import login_required, current_user
from app.services.encryption import EncryptionService
from app.models.file import File

file_bp = Blueprint('file', __name__, template_folder='templates')

@file_bp.route('/upload', methods=['GET'])
@login_required
def upload_page():
    return render_template('upload.html')

@file_bp.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        flash('No file part in the request')
        return redirect(url_for('file.upload_page'))
        
    file = request.files['file']
    
    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('file.upload_page'))
    try:
        encrypted_folder = current_app.config['ENCRYPTED_FILE_PATH']
        if not os.path.exists(encrypted_folder):
            os.makedirs(encrypted_folder)
        
        file_id = str(uuid.uuid4())
        filename = file.filename
        file_path = os.path.join(encrypted_folder, file_id + "_" + filename)
        encrypter = EncryptionService()
        encrypter.encrypt(file, file_path)
        
        
        File.add_file(
            filename=filename,
            filepath=file_path,
            file_id=file_id,
            owner_id=current_user.id
        )
        
        flash('File uploaded and encrypted successfully')
        return redirect(url_for('file.upload_page'))
    
    except Exception as e:
        flash(f'Error uploading file: {str(e)}')
        return redirect(url_for('file.upload_page'))