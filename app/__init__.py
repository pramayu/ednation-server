from flask import Flask
from flask_cors import CORS
from app.config import DevelopmentConfig
from flask_mongoengine import MongoEngine


app = Flask(__name__)
CORS(app)
app.config.from_object(DevelopmentConfig)
db = MongoEngine(app)
