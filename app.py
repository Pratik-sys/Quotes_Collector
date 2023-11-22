from flask import Flask
from flask_restx import Api, Resource
from mongoengine import connect
from models import Quotes

app = Flask(__name__)
api = Api(app)

connect(host="mongodb://127.0.0.1:27017")

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
        Quotes(title="test1", author="testauthor").save()
        return {"msg": "dumped"}

if __name__ == "__main__":
    app.run(port=8080, debug=True)
    # End-of-file (EOF)
