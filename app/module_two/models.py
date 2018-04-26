from database import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Item(Base):
    __tablename__ = 'items'

    name = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name
