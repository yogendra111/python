from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://myuser:mypassword@localhost/pythondb"
db = SQLAlchemy(app)
ma = Marshmallow(app)
auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme='Bearer')

USER_DATA = {
    "admin": generate_password_hash("password")
}

# from AuthWithFlaskLogin import routes
from AuthAPIs import routes  # this is for component scan
