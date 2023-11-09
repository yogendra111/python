from AuthAPIs import app, auth


@app.route('/private')
@auth.login_required
def private():
    return "Hello, {}!".format(auth.current_user())

# app.add_url_rule("/private", PrivateResource)
