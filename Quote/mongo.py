from mongoengine import connect
from flask import Flask

app = Flask(__name__)

class MongoEngine:
    """Class that has functionality to init the db and raise error if any"""

    def init_db(self, constring):
        """funciton to init DB connection"""
        try:
            if constring:
                print("Connection string found, connecting to database")
                app.logger.info("Connection string found, connecting to database")
                connect(host=constring)
            else:
                app.logger.error("No connection String provided")
                raise ConnectionAbortedError
        except Exception as ex:
            raise ConnectionRefusedError from ex
    
        