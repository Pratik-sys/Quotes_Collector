from mongoengine import  StringField, Document

class Quotes(Document):
    title = StringField()
    author = StringField()