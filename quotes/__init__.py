""" A small flask Hello World """

import os
import logging

from flask import Flask, jsonify, session, redirect, url_for
from flask import make_response, request, render_template
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)

# Load default configuration and any environment variable overrides
_root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
APP.config.from_pyfile(os.path.join(_root_dir, 'config.env.py'))

# Load file based configuration overrides if present
_pyfile_config = os.path.join(_root_dir, 'config.py')
if os.path.exists(_pyfile_config):
    APP.config.from_pyfile(_pyfile_config)

# Logger configuration
logging.getLogger().setLevel(APP.config['LOG_LEVEL'])
logging.getLogger().info('Launching rit-sse-api')

db = SQLAlchemy(APP)
logging.getLogger().info('SQLAlchemy pointed at ' + repr(db.engine.url))

from . import models
from .models import Quote

db.create_all()

@APP.route('/')
def _get_index():
    return render_template('index.html', quotes=reversed(Quote.get_approved()))