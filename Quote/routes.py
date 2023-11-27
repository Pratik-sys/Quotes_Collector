import json
from Quote.models import Quotes
from Quote.extension import api, app
from flask_restx import Resource
from flask import request, jsonify
from Quote.validation import validateQuotes, validateUpdateQuotes
from flask import Flask

@api.route("/AddQ")
class AddQuotes(Resource):
    def post(self):
        """POST req to add details in Database"""
        record = json.loads(request.data)
        app.logger.info(
            "User inputs >>>  Title : %s, Author: %s ",
            record["title"],
            record["author"],
        )
        try:
            quote = Quotes(title=record["title"], author=record["author"])
            app.logger.info("Validating JSON")
            error = validateQuotes(quote)
            if len(error) == 0:
                if quote.author == "":
                    app.logger.warning(
                        "Author field is blank, default set to Anonymous"
                    )
                    quote.author = "Anonymous"
                app.logger.info(
                    " Saving data in DB >>> Title : %s,  Author : %s",
                    quote.title,
                    quote.author,
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
    def put(self, qid: str):
        """PUT req to update any records in database or particular objectID"""
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
            error = validateUpdateQuotes(record)
            if len(error) == 0:
                quote.modify(
                    title=record["title"] or quote.title,
                    author=record["author"] or quote.author,
                )
                app.logger.warning(
                    "Note : if any of the fields are not udpated with new data, DB would be saved with old data"
                )
                app.logger.info(
                    "New updated fields are %s , %s",
                    record["title"] or quote.title,
                    record["author"] or quote.author,
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
    def delete(self, qid: str):
        """DEL req to delete particular quote with refrence to objectID"""
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
