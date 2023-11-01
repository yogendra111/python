from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://myuser:mypassword@localhost/pythondb"
app.config['SECRET_KEY'] = "998a0c50bb4a6240e9c83f7cc713d46ea6ca2f91c2a45b54a6d5c3cf61aa005e"
db = SQLAlchemy(app)
ma = Marshmallow(app)

# from modals import User, Blog
from AuthApp import routes
