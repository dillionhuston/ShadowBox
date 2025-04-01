#USER auth routes (sign-up, login, )
from flask import Blueprint
from flask_login import *
#import some more

auth_bp = Blueprint('auth', __name__)

class Auth():

    def __init__(self, app):
        self.app = app
        self.app.register_blueprint(auth_bp)


    @auth_bp.route('/signup')
    def signup(self):
        return 200