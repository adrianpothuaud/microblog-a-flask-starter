from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    # Mock User
    user = {"username": "adrian"}
    # Renders a template
    return render_template("index.html", title="Home", user=user)
