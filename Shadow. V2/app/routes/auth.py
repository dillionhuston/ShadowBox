from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.user import User

# Define the Blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        if not username or not password or not email:

            flash('All fields are required.')
            return redirect(url_for('auth.signup'))
        
        # Add the user to the database
        user = User.add_user(username, email, password)

        if user:
            flash('User registered successfully! Please log in.')
            return redirect(url_for('auth.login'))  
        else:
            flash('Something went wrong. Please try again.')

    return render_template('signup.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        
        if user and User.verify_hash(password, user.password):
            flash('Login successful!')
            return render_template('dashboard.html')
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))
