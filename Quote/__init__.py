import os
from flask import Flask
from flask_restx import Api, Resource
from mongoengine import connect
from dotenv import load_dotenv
from logging.config import dictConfig
from Quote.extension import api
from Quote import routes

def create_app():
    app = Flask(__name__)
    api._init_app(app)
    load_dotenv(".env")
    connect(host=os.getenv("MONGO_URI"))
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
