from datetime import datetime
from mongoengine import StringField, Document, DateField

class Quotes(Document):
    """Models to define Schema in Monogo"""

    Title = StringField()
    Author = StringField()
    Date = DateField(default=datetime.utcnow)
