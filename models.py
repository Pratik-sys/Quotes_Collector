from mongoengine import *

class Quotes(Document):
    title = StringField()
    author = StringField()