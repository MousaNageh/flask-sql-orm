from db import db


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.DECIMAL(precision=3), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    store = db.relationship('Store', back_populates='items')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<{self.__class__.__name__}>(id: {self.id}, name: {self.name!r})'
