"""
The flask application package.
"""

from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://wph20081:wisconsinmadison@cluster0.n8zd8.mongodb.net/mydb?retryWrites=true&w=majority'
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
mongo = PyMongo(app)

import Spike.views
