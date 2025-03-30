from flask import Flask, render_template, request, redirect
import os 
from werkzeug.utils import secure_filename
from backend.db import db_operations
from backend.crypto import cryptomanager
from backend.auth import auth 
from backend.storage import storage

app = Flask(__name__, template_folder='frontend/templates')

#FOLDERS 
allowed_extension = {'.doc', 'pdf', '.py', '.zip', '.7z', '.png'} #this is for an example

# CLASS OBJECTS
backend = db_operations()
backend_auth = auth()
cryptomanager = cryptomanager()
storage = storage()


def allowed_file(filename):
     return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extension

# INDEX ROUTE
@app.route('/')
def index():
    return render_template('index.html')


# SIGN UP
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        if username and password and email:
            hashed_password = auth.hash_password(password)
            backend.adduser(username, hashed_password, email)  
            return redirect('/login') 
    return render_template('signup.html')

# LOGIN 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user = backend.get_user(username)
            return user
        passw = backend_auth.verify_password(password)
        if user and passw:
                # session variable needed
                    print("User logged in")
    return render_template("dashboard.html")

#UPLOAD 
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    
    if request.method and 'file' not in request.files == 'POST':
        return "No file uploaded", 400  
    file = request.files['file'] 
    if file: 
            storage.save_file(file)
            return "File uploaded successfully!", 200
    
    #return to dash


#DASHBOARD 
@app.route('/dashboard')
def dashboard():
     return render_template('dashboard.html')

