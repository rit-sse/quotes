import secrets
import os

# Values in this file are loaded into the flask app instance, `demo.APP` in this
# demo. This file sources values from the environment if they exist, otherwise a
# set of defaults are used. This is useful for keeping secrets secret, as well
# as facilitating configuration in a container. Defaults may be overriden either
# by defining the environment variables, or by creating a `config.py` file that
# contains locally set secrets or config values.


# Defaults for flask configuration
IP = os.environ.get('IP', default='127.0.0.1')
PORT = os.environ.get('PORT', default=5000)
SERVER_NAME = os.environ.get('SERVER_NAME', default='localhost:5000')
SECRET_KEY = os.environ.get('SESSION_KEY', default='a0e8d8d03e848472f3c1776def13bc49')
LOG_LEVEL = os.environ.get('LOG_LEVEL', default='INFO')

SQLALCHEMY_DATABASE_URI = os.environ.get('POLLER_DATABASE_URI',
    default='postgresql://postgres:password1@localhost/postgres')
SQLALCHEMY_TRACK_MODIFICATIONS = False
