"""Flask configuration."""
from os import path

# -- get path
basedir = path.abspath(path.dirname(__file__))

# -- Test & Debug
TESTING = True
DEBUG = True


# -- Flask
# FLASK_APP = 'wsgi.py'
FLASK_ENV = 'development'
#SECRET_KEY = 'xxx'

# -- Database


# -- Application
#UPLOAD_FOLDER = '/xxx'