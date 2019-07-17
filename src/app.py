from flask import Flask

from .config import app_config
from .models import db, bcrypt
from .views.NluView import nlu_api as nlu_blueprint


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    # initializing bcrypt
    bcrypt.init_app(app)  # add this line

    db.init_app(app)  # add this line
    app.register_blueprint(nlu_blueprint, url_prefix='/api/v1/nlu')  # add this line

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Congratulations! Your first endpoint is workin'

    return app
