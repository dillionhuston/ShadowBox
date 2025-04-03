from flask import Flask, Blueprint, render_template

# Define the Blueprint
auth = Blueprint('auth', __name__)

#templates 
app = Flask(__name__,template_folder='templates')

@auth.route('/signup')
def signup():
    return render_template('signup.html')  # Renders the signup form

@auth.route('/login')
def login():
    return "Login Page"

@auth.route('/logout')
def logout():
    return "Logout Page"
