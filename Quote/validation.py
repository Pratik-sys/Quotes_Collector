from Quote.models import Quotes
from Quote.extension import app


def validate_quotes(quote):
    """function will validate the data coming from JSON"""
    errors = []
    if quote.title == "":
        errors.append("Title field cannot be empty")
        app.logger.warning("Title field is empty, return the error array")
    return errors

def validate_update_quotes(record):
    """function will check for the fileds while updating in database"""
    errors = []
    if record["title"] == "":
        errors.append("Cannot update title as blank field")
        app.logger.warning("Cannot update title as blank field, retur the error array")
    return errors

