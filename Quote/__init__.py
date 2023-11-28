import os
from logging.config import dictConfig
from mongoengine import connect
from dotenv import load_dotenv
from Quote.extension import api, app
from Quote.routes import ns


def create_app():
    """function will init flask app instance at the start the server,and all the config defined under it"""
    api._init_app(app)
    load_dotenv(".env")
    connect(host=os.getenv("MONGO_URI"))
    api.add_namespace(ns)
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
