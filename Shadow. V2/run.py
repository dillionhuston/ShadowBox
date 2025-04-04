from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.routes.auth import auth_bp
from app.routes.file import file_bp
from app.models.user import db

# inits 
app = Flask(__name__, template_folder='app/templates')
app.config.from_object(Config)
db.init_app(app)

#key 
app.config['SECRET_KEY'] = '11/0bb4^95ef94aeTo95be88b27b1173857d9b32c3f'


#Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(file_bp)

#just basic secuirty.further improved soon
@app.after_request
def apply_csp(response: Response):
    # Apply a basic Content Security Policy
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self';"
    return response


if __name__ == "__main__":
    app.run(debug=True)
