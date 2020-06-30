from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#db = SQLAlchemy()
#SQLALCHEMY_TRACK_MODIFICATIONS = True
wsgi_app = app.wsgi_app
app.config.from_object(Config)
from app import routes
import config
