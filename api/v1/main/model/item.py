# import sqlite3
from database import db


class ItemModel(db.Model):
    # define tablename and parameters for SQLAlchemy
    tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        # parameters, must be same as before for SQL
        self.id = id
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        # SQLAlch way yof SELECTing
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)