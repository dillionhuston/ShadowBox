from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.routes.auth import auth
from app.routes import dashboard, file
from app.models.user import db



# inits 
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.config['SECRET_KEY'] = '11/0bb4^95ef94aeTo95be88b27b1173857d9b32c3f'



#Register blueprints
app.register_blueprint(auth)
app

@app.before_request
def create_database():
     db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
