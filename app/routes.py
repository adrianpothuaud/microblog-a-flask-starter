from datetime import datetime
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse

from app import app, db
from app.forms import EditProfileForm, LoginForm, RegistrationForm
from app.models import User


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


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


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("pages/register.html", title="Register", form=form)


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


@app.route("/users/<username>")
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    user_posts_mock = [
        {"author": {"username": user.username}, "body": "A beautiful day in Portland!"},
        {"author": {"username": user.username}, "body": "The Avengers movie was so cool!"},
    ]
    return render_template("pages/user.html", posts=user_posts_mock, user=user)


@app.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template("pages/edit_profile.html", title="Edit Profile", form=form)
