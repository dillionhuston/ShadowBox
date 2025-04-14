# Database.py
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from typing import Optional
import utils  # Ensure this is imported if using `TryWithLogErrorDecorator`

class Database:
    """A static class to manage the database."""

    db: SQLAlchemy = SQLAlchemy()
    """The SQL Alchemy instance used to access the database. Should only be one instance throughout the app."""

    @staticmethod
    @utils.TryWithLogErrorDecorator(errorReturn=False, functionName="Database.Initialize")
    def Initialize(app: Flask) -> bool:
        """Initialize the database and create the tables."""
        Database.db.init_app(app)
        with app.app_context():  # Ensure the app context is active
            Database.db.create_all()
        return True
