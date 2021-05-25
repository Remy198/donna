from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import environ
from .routes import generator


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL') or 'sqlite:///myDB.db' #path to database and its name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning

db = SQLAlchemy(app) #database instance

app.register_blueprint(generator)