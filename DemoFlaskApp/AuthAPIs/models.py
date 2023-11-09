from AuthAPIs import db, app


# UserModel
# UserMixin, which will help to implement properties such as is_authenticated to the Users class.
# db.Model, your User class becomes an SQLAlchemy model. ORM mapped
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # This is toString or representation
    def __repr__(self):
        return f'<User {self.username}>'


with app.app_context():
    db.create_all()
