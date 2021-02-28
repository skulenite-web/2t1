from flask import Flask
from flask_pymongo import pymongo

app = Flask(__name__)
app.config.from_object('cfg.DevConfig')

from app import routes
