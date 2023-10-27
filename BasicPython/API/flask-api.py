from flask import Flask, request, jsonify, redirect, url_for, render_template
from User import User as userEntity

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/admin")
def hello_admin():
    return 'Welcome User'


@app.route('/guest/<guest>')
def hello_guest(guest):  # binding to hello_guest call
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':  # dynamic binding of URL to function
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


@app.route("/user")
def user():
    newuser = userEntity("Rohit", "1234")
    my_dict = {
        "name": newuser.getName(),
        "password": newuser.getPassword()
    }
    return jsonify(my_dict)


# GET
# PUT
# POST
# DELETE


if __name__ == "__main__":
    app.run(debug=True)  # this will run flask server
