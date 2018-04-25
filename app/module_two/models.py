from database import db


class Table(db.model):
    __tablename__ = 'table_two'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name
