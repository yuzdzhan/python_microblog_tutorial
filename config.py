import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1234567890-qwertyuiop[asdfghjkl;zxcvbnm,.'
