import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# get the database url from the environment variable set in the docker-compose for the web container
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
