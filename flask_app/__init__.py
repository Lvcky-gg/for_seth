
from flask import Flask
from flask_migrate import Migrate


from models import db, example
from .config import Config
from .routes.example_route import example
from seeds import seed_commands

def create_app():
    app = Flask(__name__, static_folder="route_to_frontend_build", static_url_path="/")
    app.config.from_object(Config)
    app.cli.add_command(seed_commands)
    app.register_blueprint(example, url_prefix="/")

    db.init_app(app)
    Migrate(app, db)
    return app

app = create_app()