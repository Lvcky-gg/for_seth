from models import db, Example, environment, SCHEMA
from sqlalchemy.sql import text

def seed_examples():
    one = Example(
        example_text="THIS IS A TEST"
    )
    db.session.add(one)
    db.session.commit()

def undo_examples():

    db.session.execute(text("DELETE FROM examples"))

    db.session.commit()   