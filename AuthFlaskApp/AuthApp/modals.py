from AuthApp import db, app

from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), default='user')

    def __repr__(self):
        return f'<User {self.id} {self.username}>'


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    def __repr__(self):
        return f'<Blog(id={self.id}, title={self.title}, description={self.description}, date={self.date})>'


with app.app_context():
    db.create_all()
