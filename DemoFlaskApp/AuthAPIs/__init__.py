from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://myuser:mypassword@localhost/pythondb"
db = SQLAlchemy(app)
ma = Marshmallow(app)
auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme='Bearer')

# from AuthWithFlaskLogin import routes
