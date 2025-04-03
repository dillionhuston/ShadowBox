from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.routes.auth import auth
from app.routes import dashboard, file

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

#Register blueprints
app.register_blueprint(auth)
app


with app.app_context():
    db.create_all()  

if __name__ == "__main__":
    app.run(debug=True)
