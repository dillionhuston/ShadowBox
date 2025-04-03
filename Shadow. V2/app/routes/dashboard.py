#user dashboard (list files, manage uploads )
from flask import Blueprint
dash_bp = Blueprint('dash', __name__)

class Dashboard():

    def __init__(self, app):
        self.app = app
        self.app.register_blueprint(Dashboard)


    @dash_bp.route('/dashbaord')
    def signup(self):
        return 200