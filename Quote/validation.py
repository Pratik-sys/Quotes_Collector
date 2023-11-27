from Quote.models import Quotes
from Quote.extension import app


def validateQuotes(quote):
    errors = []
    if quote.title == "":
        errors.append("Title field cannot be empty")
        app.logger.warning("Title field is empty, return the error array")
    return errors

def validateUpdateQuotes(record):
    errors = []
    if record["title"] == "":
        errors.append("Cannot update title as blank field")
        app.logger.warning("Cannot update title as blank field, retur the error array")
    return errors

