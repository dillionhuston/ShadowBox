from flask import Flask, render_template, request, redirect
from backend.db import db_operations
from backend.auth import auth 

app = Flask(__name__, template_folder='frontend/templates')


backend = db_operations()

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
            # Hash the password before storing
            hashed_password = auth.hash_password(password)
            backend.adduser(username, hashed_password, email)  
            return redirect('/login') 
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/upload')
def upload():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
