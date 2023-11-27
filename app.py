import os, json, boto3
from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from mongoengine import connect
from validation import validateQuotes, validateUpdateQuotes
from dotenv import load_dotenv
from models import Quotes
from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "flask.log",
                "formatter": "default",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["console", "file"]},
    }
)

app = Flask(__name__)
api = Api(app)
load_dotenv(".env")
connect(host=os.getenv("MONGO_URI"))
# session = boto3.Session(
#     aws_access_key_id=os.getenv("ACCESS_KEY"),
#     aws_secret_access_key=os.getenv("SECRETE_KEY")
# )

# s3 = boto3.client('s3', aws_access_key_id= os.getenv("ACCESS_KEY") , aws_secret_access_key=os.getenv("SECRETE_KEY"))
# s3.download_file(os.getenv("BUCKET_NAME"), os.getenv("OBJECT"), os.getenv("DOWNLOAD_PATH"))
# s3.upload_file(os.getenv("UPLOAD_PATH"), os.getenv("BUCKET_NAME"), os.getenv("OBJECT"))


@api.route("/AddQ")
class AddQuotes(Resource):
    def post(self):
        """POST req to add details in Database"""
        record = json.loads(request.data)
        try:
            quote = Quotes(title=record["title"], author=record["author"])
            app.logger.info("hello world")
            error = validateQuotes(quote)
            if len(error) == 0:
                if quote.author == "":  
                    print("Author field is blank, default set to Anonymous")
                    quote.author = "Anonymous"
                    quote.save()
                    return jsonify({"Msg": "Quotes dumped"}, 200)
            else:
                return jsonify(error, 404)
        except Exception as ex:
            return jsonify(ex, 404)


@api.route("/<string:qid>/UpdateQ")
class UpdateQuotes(Resource):
    def put(self, qid: str):
        """PUT req to update any records in database or particular objectID"""
        try:
            q = Quotes.objects(id=qid).first()
            record = json.loads(request.data)
            error = validateUpdateQuotes(record)
            if len(error) == 0:
                q.modify(
                    title=record["title"] or q.title,
                    author=record["author"] or q.author,
                )
                return jsonify({"Msg": "Quote is updated"}, 200)
            else:
                return jsonify(error, 404)
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
