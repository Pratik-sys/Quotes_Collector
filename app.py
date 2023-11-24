import os, json,boto3
from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from mongoengine import connect
from dotenv import load_dotenv
from models import Quotes

app = Flask(__name__)
api = Api(app)
load_dotenv(".env")
connect(host=os.getenv("MONGO_URI"))
session = boto3.Session(
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRETE_KEY")
)

s3 = boto3.client('s3', aws_access_key_id= os.getenv("ACCESS_KEY") , aws_secret_access_key=os.getenv("SECRETE_KEY"))
s3.download_file(os.getenv("BUCKET_NAME"), os.getenv("OBJECT"), os.getenv("OS_PATH"))

@api.route("/AddQ")
class AddQuotes(Resource):
    def post(self):
        """POST req to add details in Database"""
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


@api.route("/<string:qid>/UpdateQ")
class UpdateQuotes(Resource):
    def put(self, qid: str):
        """PUT req to update any records in database or particular objectID"""
        try:
            q = Quotes.objects(id=qid).first()
            record = json.loads(request.data)
            q.modify(title=record["title"], author=record["author"])
            return jsonify({"Msg": "Fields are updated"})
        except Exception as ex:
            return jsonify({"Msg": ex})


@api.route("/<string:qid>/DelQ")
class DeleteQuotes(Resource):
    def delete(self, qid: str):
        """DEL req to delete particular quote with refrence to objectID"""
        try:
            q = Quotes.objects(id=qid).first()
            if q is not None:
                q.delete()
                return jsonify({"Msg": f"Quote with {qid} deleted"})
            else:
                return jsonify({"Msg": f"No quote with {qid} to delete"})
        except Exception as ex:
            return jsonify({"Msg": ex})


if __name__ == "__main__":
    app.run(port=8080, debug=True)
    # End-of-file (EOF)
