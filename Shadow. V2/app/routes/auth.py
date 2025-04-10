from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.user import User

# Define the Blueprint
auth_bp = Blueprint('auth', __name__)

# Sign Up Page (GET)
@auth_bp.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

# Handle Sign Up (POST)
@auth_bp.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email is already taken. Please use a different email address.')
            return redirect(url_for('auth.signup')) 

        if not username or not password or not email:
            flash('All fields are required.')
            return redirect(url_for('auth.signup')) 

        user = User.add_user(username, email, password)
        if user:
            flash('User registered successfully! Please log in.')
            return redirect(url_for('auth.login'))  
        else:
            flash('Something went wrong. Please try again.')

    return render_template('signup.html')

# Login Page (GET)
@auth_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

# Handle Login (POST)
@auth_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and User.verify_hash(password, user.password):
            flash('Login successful!')
            # add session id here flask-login
            return ('dashboard.html') #change to redirect
        else:
            flash('Invalid username or password.')

    return render_template('login.html')

# Logout
@auth_bp.route('/logout')
def logout():
    session.clear()  
    flash('You have been logged out successfully.')
    return login_page()
