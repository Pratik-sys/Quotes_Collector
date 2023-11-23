import os, json
from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from mongoengine import connect
from dotenv import load_dotenv
from models import Quotes


app = Flask(__name__)
api = Api(app)
load_dotenv(".env")
connect(host=os.getenv("MONGO_URI"))


@api.route("/AddQ")
class AddQuotes(Resource):
    def post(self):
        """Post req to add details in Database"""
        record = json.loads(request.data)
        try:
            if len(record) != 0:
                quote = Quotes(title=record["title"], author=record["author"])
                quote.save()
                return jsonify({"Msg": "data is dumped"}, 200)
            else:
                return jsonify({"Msg": "Fields are empty"}, 201)
        except Exception as ex:
            return jsonify({"Msg": ex}, 404)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
    # End-of-file (EOF)
