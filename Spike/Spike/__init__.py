"""
The flask application package.
"""

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://wph20081:wisconsinmadison@cluster0.qztag.mongodb.net/mydb?retryWrites=true&w=majority'

mongo = PyMongo(app)

import Spike.views
