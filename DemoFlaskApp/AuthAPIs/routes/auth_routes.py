from werkzeug.security import check_password_hash

from AuthAPIs import auth, USER_DATA, app


@app.route('/private')
@auth.login_required
def private():
    return "Hello, {}!".format(auth.current_user())


# app.add_url_rule("/private", PrivateResource)


@auth.verify_password
def verify(username, password):
    if username in USER_DATA and \
            check_password_hash(USER_DATA.get(username), password):
        return username
# def verify(username, password):
#     if not username and password:
#         return False
#     return USER_DATA.get(username) == password
