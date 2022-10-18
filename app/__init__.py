from flask import Flask

from config import Config

# Creates the application object as instance of class Flask
app = Flask(__name__)

# Application configuration
app.config.from_object(Config)

# Import at the bottom to resolve circular dependencies
from app import routes
