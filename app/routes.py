from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse

from app import app
from app.forms import LoginForm
from app.models import User


@app.route("/")
@app.route("/index")
@login_required
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
    return render_template("pages/index.html", posts=posts, title="Home")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("pages/login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
