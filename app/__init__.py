from flask import Flask

# Creates the application object as instance of class Flask
app = Flask(__name__)

# Import at the bottom to resolve circular dependencies
from app import routes