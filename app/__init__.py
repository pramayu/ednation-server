from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from app.config import DevelopmentConfig
from flask_mongoengine import MongoEngine
from app.api import schema


app = Flask(__name__)
CORS(app)
app.config.from_object(DevelopmentConfig)
db = MongoEngine(app)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))