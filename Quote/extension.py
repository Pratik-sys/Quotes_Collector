from flask_restx import Api
from Quote.mongo import MongoEngine

api = Api()
db = MongoEngine()