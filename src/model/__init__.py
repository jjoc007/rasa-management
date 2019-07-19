#src/model/__init__.py

from flask_sqlalchemy import SQLAlchemy
# from src.app import flask_app

# initialize our db
db = SQLAlchemy()

from flask_bcrypt import Bcrypt
#######
# existing code remains #
#######
bcrypt = Bcrypt()