import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    ADMINS = ["your-email@example.com"]
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    SECRET_KEY = os.getenv("SECRET_KEY") or "you_will_never_guess"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
