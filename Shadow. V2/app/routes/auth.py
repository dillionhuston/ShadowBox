from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, current_user, login_required, logout_user
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

# Sign Up Page (GET)
@auth_bp.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')



# Handle Sign Up (POST)
@auth_bp.route('/signup', methods=['POST'])
def signup():
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

    try:
        newuser = User.add_user(username, email, password)
        flash('User registered successfully! Please log in.')
        return redirect(url_for('auth.login'))
    except Exception as e:
        flash(f'Registration failed: {str(e)}')
        
    return render_template('signup.html')



# Login Page (GET)
@auth_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')



# Handle Login (POST)
@auth_bp.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('file.upload_page'))
    
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    
    if user and User.verify_hash(password, user.password):
        login_user(user)
        flash('Login successful!')
        session['user_key'] = user.key  # Store encryption key in session
        return redirect(url_for('file.upload_page'))
    else:
        flash('Invalid username or password.')
    
    return render_template('login.html')


# Logout
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash('You have been logged out successfully.')
    return redirect(url_for('auth.login_page'))