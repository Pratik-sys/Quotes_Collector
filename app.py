from flask import Flask
from flask_restx import Api, Resource


app = Flask(__name__)
api = Api(app)


@api.route("/test")
class TestAPI(Resource):
    """This API just for testing purpose"""

    def get(self):
        """Get req to check whether api returns the defined response"""
        return {"msg": "Testing API"}


if __name__ == "__main__":
    app.run(port=8080, debug=True)
    # End-of-file (EOF)
