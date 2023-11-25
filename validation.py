from models import Quotes

def validateQuotes(quote):
    errors = []
    if quote.title == "":
        errors.append("Title cannot be empty")
    return errors

def validateUpdateQuotes(record):
    errors = []
    if record["title"] == "":
        errors.append("Cannot update title blank")
    return errors