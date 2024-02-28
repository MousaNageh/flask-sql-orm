from db import db


class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text, nullable=False)
    items = db.relationship('Item', back_populates='store', cascade='all, delete', lazy='dynamic')
    tags = db.relationship('Tag', back_populates='store', cascade='all, delete', lazy='dynamic')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<{self.__class__.__name__}>(id: {self.id}, name: {self.name!r})'
