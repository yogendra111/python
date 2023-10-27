from AuthWithFlaskLogin import login_manager, db, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# UserModel
# UserMixin, which will help to implement properties such as is_authenticated to the Users class.
# db.Model, your User class becomes an SQLAlchemy model. ORM mapped
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    # This is toString or representation
    def __repr__(self):
        return f'<User {self.username}>'


with app.app_context():
    db.create_all()
