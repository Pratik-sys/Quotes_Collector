import os, json
from flask import Flask, request
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


@api.route("/AddQ")
class AddQuotes(Resource):
    """This API just for testing purpose"""

    def post(self):
        """Post req to add in DB"""
        record = json.loads(request.data)
        try:
            if len(record) != 0:
                quote = Quotes(title=record["title"], author=record["author"])
                quote.save()
                return {"msg":"data is dumped"}
            else:
                return {"msg": "Fields are empty"}
        except:
            return {"msg": "something is wrong"}


if __name__ == "__main__":
    app.run(port=8080, debug=True)
    # End-of-file (EOF)
