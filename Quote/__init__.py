import os
from logging.config import dictConfig
from flask import Flask
from dotenv import load_dotenv
from Quote.extension import api, db
from Quote import routes

def create_app():
    """function will init flask app instance at the start the 
    server,and all the config defined under it"""
    app = Flask(__name__)
    api._init_app(app)
    load_dotenv(".env")
    db.init_db(os.getenv("MONGO_URI"))
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                    "formatter": "default",
                },
                "size-rotate": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": "flask.log",
                    "maxBytes": 1000000,
                    "backupCount": 5,
                    "formatter": "default",
                },
            },
            "root": {"level": "DEBUG", "handlers": ["console", "size-rotate"]},
        }
    )
    return app
