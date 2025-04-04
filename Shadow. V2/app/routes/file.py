# file upload/download/decryption routes
from flask import Blueprint, render_template, url_for, redirect, request, Response
file_bp = Blueprint('file', __name__, template_folder='templates')



class Files():
    """its better to sperate into two functions rather than one """
    @file_bp.route('/upload', methods=['GET'])
    def upload_page():
            return render_template('upload.html')
    
    @file_bp.route('/upload', methods=['POST'])
    def upload_file():
            file = request.files['file']
            filename = file.filename
            file.save(filename) # dedbug. implemetn file encryption
            print(file)
            return render_template('dashboard.html', filename=filename)
        