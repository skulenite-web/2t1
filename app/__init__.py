import os
from flask import Flask
from flask_pymongo import pymongo

app = Flask(__name__)
app.config.from_object(os.environ['CONFIG'])

from app import routes
