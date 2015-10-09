import datetime
from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('lcbru_events.settings')

ADMINS = ['rab63@le.ac.uk']

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler('127.0.0.1',
                               'lcbruit@le.ac.uk',
                               ADMINS, 'YourApplication Failed')
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

if not app.debug:
    import logging
    from logging.handlers import FileHandler
    file_handler = FileHandler('error.log')
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

db = SQLAlchemy(app)

import lcbru_events.database
database.init_db()

app.secret_key = app.config['SECRET_KEY']

@app.before_request
def set_date():
    g.year = datetime.datetime.now().year

import lcbru_events.helpers.templateFilters

from lcbru_events.views import *
