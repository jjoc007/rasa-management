import os

from src.app import create_app
from src.files import initializer

if __name__ == '__main__':
  env_name = os.getenv('FLASK_ENV')
  app = create_app(env_name)

  #crear carpetas si no existen
  initializer.initialize_folders()

  # run app
  app.run()