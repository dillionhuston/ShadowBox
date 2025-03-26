from flask import Flask, render_template, request, redirect
from backend.db import db_operations
from frontend.templates import *   # Correct import from frontend package

template_dir = 'frontend/templates'
backend = db_operations()

app = Flask(__name__, template_folder=template_dir)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST': 
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        if username and password and email:
            backend.adduser(username, password, email) 
            return redirect('/login')

    return render_template('signup.html')

    
@app.route('/login')
def login():
    return render_template("login.html")






   