from flask import Flask

# from src.config import app_config
# from src.model import db, bcrypt
# from src.controller.NluView import nlu_api as nlu_blueprint
from flask_restplus import Api, Resource

# app initiliazation
flask_app = Flask(__name__)
app = Api(app=flask_app)
name_space = app.namespace('main', description='Api para la administracion de Chat-Bot')
# app.config.from_object(app_config("development"))

@name_space.route("/")
class MainClass(Resource):

    def get(self):
        return {
            "status": "Got new data"
        }

    def post(self):
        return {
            "status": "Post new data"
        }


def create_app(env_name):
    """
    Create app
    """
    # app.register_blueprint(nlu_blueprint, url_prefix='/api/v1/nlu')  # add this line
    """
    @app.route('/', methods=['GET'])
    def index():
       
        example endpoint
       
        return 'Congratulations! Your first endpoint is workin'
    """

    return app

flask_app.run()