from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

flask_app = Flask(__name__)
flask_app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo = PyMongo(flask_app)
db = mongo.cx.MovieCraze
