from flask import Flask
from models import Quotes

app = Flask(__name__)

def validateQuotes(quote):
    errors = []
    if quote.title == "":
        errors.append("Title cannot be empty")
        app.logger.warning("Title is empty returning the error array")
    return errors

def validateUpdateQuotes(record):
    errors = []
    if record["title"] == "":
        errors.append("Cannot update title blank")
        app.logger.warning("Cannot update title blank returning the error array")
    return errors

