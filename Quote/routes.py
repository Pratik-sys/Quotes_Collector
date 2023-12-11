import json
from flask import Flask, request, jsonify
from flask_restx import Resource
from Quote.models import Quotes
from Quote.extension import api
from Quote.validation import validate_quotes, validate_update_quotes

app = Flask(__name__)
@api.route("/GetQ")
class GetAllQuotes(Resource):
    """Endpoint to fetch all the records from the database"""

    def get(self):
        quote = Quotes.objects.to_json()
        if len(quote) > 2:
            app.logger.info(quote)
            return jsonify(quote, 200)
        else:
            app.logger.warning("No quotes to display")
            return jsonify({"Msg": "No quotes to display"})


@api.route("/AddQ")
class AddQuotes(Resource):
    """Endpoint with POST method to insert documnet in collections"""

    def post(self):
        record = json.loads(request.data)
        app.logger.info(
            "User inputs >>>  Title : %s, Author: %s ",
            record["title"],
            record["author"],
        )
        try:
            quote = Quotes(Title=record["title"], Author=record["author"])
            app.logger.info("Validating JSON")
            error = validate_quotes(quote)
            if len(error) == 0:
                if quote.Author == "":
                    app.logger.warning(
                        "Author field is blank, default set to Anonymous"
                    )
                    quote.Author = "Anonymous"
                app.logger.info(
                    " Saving data in DB >>> Title : %s,  Author : %s",
                    quote.Title,
                    quote.Author,
                )
                quote.save()
                return jsonify({"Msg": "Quote added"}, 200)
            else:
                app.logger.error("%s", error)
                return jsonify(error, 404)
        except Exception as ex:
            app.logger.exception("%s", ex)
            return jsonify(ex, 404)


@api.route("/<string:qid>/UpdateQ")
class UpdateQuotes(Resource):
    """Endpoint With PUT method modfiy/update the exixting record with ObjectId"""

    def put(self, qid: str):
        try:
            quote = Quotes.objects(id=qid).first()
            app.logger.info("ObjectId for the requested quote is >>> %s", qid)
            record = json.loads(request.data)
            app.logger.info(
                "User inputs >>> Title : %s and Author : %s",
                record["title"],
                record["author"],
            )
            app.logger.info("Validating JSON")
            error = validate_update_quotes(record)
            if len(error) == 0:
                quote.modify(
                    Title=record["title"] or quote.Title,
                    Author=record["author"] or quote.Author,
                )
                app.logger.warning(
                    "Note : if any of the fields are not udpated with new data, DB would be saved with old data"
                )
                app.logger.info(
                    "New updated fields are %s , %s",
                    record["title"] or quote.Title,
                    record["author"] or quote.Author,
                )
                return jsonify({"Msg": "Quote is updated"}, 200)
            else:
                app.logger.error("%s", error)
                return jsonify(error, 404)
        except Exception as ex:
            app.logger.exception("%s", ex)
            return jsonify({"Msg": ex})


@api.route("/<string:qid>/DelQ")
class DeleteQuotes(Resource):
    """Endpoint with DELETE method to remove from datbase with reference to onjectID"""

    def delete(self, qid: str):
        try:
            quote = Quotes.objects(id=qid).first()
            app.logger.info("ObjectId for the requested quote is >>> %s", qid)
            if quote is not None:
                quote.delete()
                app.logger.info("Quote with ObjectID : %s, is deleted", qid)
                return jsonify({"Msg": f"Quote with {qid} deleted"})
            else:
                app.logger.warning("No quote found with objectId : %s in database", qid)
                return jsonify({"Msg": f"No quote with {qid} to delete"})
        except Exception as ex:
            app.logger.exception("%s", ex)
            return jsonify({"Msg": ex})