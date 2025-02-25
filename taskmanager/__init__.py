import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the app
app = Flask(__name__)

# Load the environment variables if the file exists
if os.path.exists('env.py'):
    import env  # noqa

# Configure the app with secret key
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Configure the SQLALCHEMY_DATABASE_URI based on the environment
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DB_URL")  # Local database URL for development
else:
    uri = os.environ.get("DATABASE_URL")
    # Adjust for compatibility with the older 'postgres://' format
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  # Set the URI for production

# Initialize the database with the app
db = SQLAlchemy(app)

# Initialize Flask-Migrate with the app and db
migrate = Migrate(app, db)

# Import your routes
from taskmanager import routes  # noqa
