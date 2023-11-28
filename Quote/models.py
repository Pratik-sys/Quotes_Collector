from datetime import datetime
from mongoengine import StringField, Document, DateField


class Quotes(Document):
    title = StringField()
    author = StringField()
    date = DateField(default=datetime.utcnow)
    # End-of-file (EOF)
