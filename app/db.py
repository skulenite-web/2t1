from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "lolfail"

# Connect
client = pymongo.MongoClient(CONNECTION_STRING)
db = client['2t1db']

# Set up collections
people = db.people
sketches = db.sketches
