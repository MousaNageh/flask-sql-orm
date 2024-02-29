from db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False, unique=True)

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<{self.__class__.__name__}(id : {self.id}, username: {self.username!r})>"
