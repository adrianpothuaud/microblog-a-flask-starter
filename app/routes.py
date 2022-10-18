from flask import render_template
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    # Mock Users
    adrian = {"username": "adrian"}
    brad = {"username": "braddy"}
    # Mock Posts
    posts = [
        {"author": {"username": adrian["username"]}, "body": "A beautiful day in Portland!"},
        {"author": {"username": brad["username"]}, "body": "The Avengers movie was so cool!"},
    ]
    # Renders a template
    return render_template("pages/index.html", posts=posts, title="Home", user=adrian)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("pages/login.html", title="Login", form=form)
