import os
import uuid
import logging
from flask import Blueprint, render_template, url_for, redirect, request, current_app, flash
from flask_login import login_required, current_user
from app.services.encryption import EncryptionService
from app.models.file import File
from config import Config


file_bp = Blueprint('file', __name__, template_folder='templates')
encrypted_folder = Config.ENCRYPTED_FILE_PATH
logger = logging.getLogger(__name__)

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
        EncryptionService.encrypt(filename=file.filename, file=file)
        flash('File uploaded and encrypted successfully')
        return redirect(url_for('file.upload_page'))
    
    except Exception as e:
        logger.error(f"Error in file upload: {str(e)}")
        flash(f'Error uploading file: {str(e)}')
        return redirect(url_for('file.upload_page'))
    
