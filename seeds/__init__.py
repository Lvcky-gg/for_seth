from flask.cli import AppGroup
from .example import seed_examples, undo_examples


# So we can type `flask seed --help`
seed_commands = AppGroup("seed")

@seed_commands.command("all")
def seed():
    seed_examples()


@seed_commands.command("undo")
def undo():
    undo_examples()
