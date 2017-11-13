import os
from celery import Celery
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

host = os.environ.get('GRABBY_HOST', '127.0.0.1')
port = os.environ.get('GRABBY_PORT', '5000')
app = Flask(__name__, static_folder='.')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grabby.db'
celery = Celery()
db = SQLAlchemy(app)
