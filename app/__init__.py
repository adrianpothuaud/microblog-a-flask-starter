from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

# Creates the application object as instance of class Flask
app = Flask(__name__)

# Application configuration
app.config.from_object(Config)

# Database instance
db = SQLAlchemy(app)

# Migrate instance
migrate = Migrate(app, db)

# Import at the bottom to resolve circular dependencies
from app import routes, models
