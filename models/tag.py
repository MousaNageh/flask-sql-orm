from db import db


class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    store = db.relationship("Store", back_populates="tags")
    items = db.relationship("Item", back_populates="tags", secondary="items_tags", cascade='all, delete', lazy='dynamic')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.__class__.__name__}(id : {self.id}, name: {self.name!r})>"
