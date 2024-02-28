from flask_sqlalchemy import SQLAlchemy

import os

environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


db = SQLAlchemy()
