from datetime import datetime
from mongoengine import StringField, Document, DateField

class Quotes(Document):
    """Models to define Schema in Monogo"""
    title = StringField()
    author = StringField()
    date = DateField(default=datetime.utcnow)
    # End-of-file (EOF)
