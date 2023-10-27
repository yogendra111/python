from AuthWithFlaskLogin import app

if __name__ == "__main__":
    app.run(debug=True)

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://myuser:mypassword@localhost/pythondb"
# app.config['SECRET-KEY'] = "Ps4k6XK0JlSVHmv7tbK0lbt9H6Mxr8gf"  # Random key generated with 256 encryption
#
# # db = SQLAlchemy()  # Deferred binding, reuse the same db object across multiple Flask applications
# db = SQLAlchemy(app)  # Immediate binding, when you have a single Flask application
# ma = Marshmallow(app)
# login_Manager = LoginManager()
# login_Manager.init_app(app)
#
# if __name__ == '__main__':
#     app.run(debug=True)
