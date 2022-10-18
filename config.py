import os


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") or "you_will_never_guess"
