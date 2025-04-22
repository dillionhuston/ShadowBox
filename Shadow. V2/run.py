from flask import Flask, Response, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from app.routes.auth import auth_bp
from app.routes.file import file_bp
from app.models import db
from app.models.user import User

app = Flask(__name__, template_folder='app/templates')
app.config.from_object(Config)
db.init_app(app)







login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

with app.app_context():
    db.create_all()

# Register route blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(file_bp)

# Basic Content Security Policy
@app.after_request
def apply_csp(response: Response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self';"
    return response

@app.route('/')
def home():
    return render_template("index.html")

@login_manager.user_loader
def load_user(user_id):
    try:
        return db.session(user_id)
    except:
        return None

if __name__ == "__main__":
    app.run(debug=True)