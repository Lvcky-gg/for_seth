from .db import db, environment, SCHEMA

class Example(db.Model):

    __tablename__="examples"
    
    id = db.Column(db.Integer, primary_key=True)
    example_text = db.Column(db.String(), nullable=False)


    def to_dict(self):
        return {
            "id":self.id,
            "example_text":self.example_text
        }