import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the app
app = Flask(__name__)

# Load the environment variables if the file exists
if os.path.exists('env.py'):
    import env  # noqa

# Configure the app with secret key and database URI
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Initialize the database with the app
db = SQLAlchemy(app)

# Initialize Flask-Migrate with the app and db
migrate = Migrate(app, db)

# Import your routes
from taskmanager import routes  # noqa
