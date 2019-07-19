import os

from src.app import create_app
from src.files import initializer
from flask_script import Manager


env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)
# crear carpetas si no existen
initializer.initialize_folders()

manager = Manager(app)


@manager.command
def run():
    app.run()
