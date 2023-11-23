import os
from flask import Flask
from flask_restx import Api, Resource
from mongoengine import connect
from dotenv import load_dotenv
from models import Quotes


app = Flask(__name__)
api = Api(app)
load_dotenv(".env")
connect(host=os.getenv("MONGO_URI"))


@api.route("/test")
class TestAPI(Resource):
    """This API just for testing purpose"""

    def get(self):
        """Get req to check whether api returns the defined response"""
        return {"msg": "Testing API"}


@api.route("/dump")
class Dumpdata(Resource):
    """This API just for testing purpose"""

    def post(self):
        """Get req to check whether api returns the defined response"""
        Quotes(title="test2", author="testauthor2").save()
        return {"msg": "dumped"}


if __name__ == "__main__":
    app.run(port=8080, debug=True)
    # End-of-file (EOF)
