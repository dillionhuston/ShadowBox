from flask import Flask, render_template, request, redirect
from backend.db import db_operations
from backend.auth import auth 

app = Flask(__name__, template_folder='frontend/templates')

backend = db_operations()
backend_auth = auth()

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
            hashed_password = auth.hash_password(password)
            backend.adduser(username, hashed_password, email)  
            return redirect('/login') 
    return render_template('signup.html')

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

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/dashboard')
def dashboard():
     return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
