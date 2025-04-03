import utils
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from typing import Optional

class Database:
    """A static class to manage the database."""
    
    db: SQLAlchemy = SQLAlchemy()
    """The SQL Alchemy use to access the database. Should only be one instance through the app."""
    
    @staticmethod
    @utils.TryWithLogErrorDecorator(errorReturn=False, functionName="Database.Initialize")
    def Initialize(app: Flask) -> bool:
        """Initialize the database and create the table."""
        Database.db.init_app(app)
        Database.db.create_all()
        return True
    
    # Database related function should be here.
    
        