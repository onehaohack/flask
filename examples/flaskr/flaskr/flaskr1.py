from datetime import datetime

from flask_stormpath import StormpathManager

from factory import create_app
from flask import Flask, abort, flash, redirect, render_template, request, url_for
#from flask.ext.stormpath import StormpathError, StormpathManager, User, login_required, login_user, logout_user, user
#from factory import create_appcreate_app


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'some_really_long_random_string_here'
app.config['STORMPATH_API_KEY_FILE'] = 'apiKey.properties'
app.config['STORMPATH_APPLICATION'] = 'flaskr'

# These settings disable the built-in login / registration / logout functionality
# Stormpath provides so we can make our own custom ones later!
app.config['STORMPATH_ENABLE_LOGIN'] = False
app.config['STORMPATH_ENABLE_REGISTRATION'] = False
app.config['STORMPATH_ENABLE_LOGOUT'] = False

stormpath_manager = StormpathManager(app)

# @app.route('/')
# def show_entries():
#     return "Hello World !!~~"

if __name__ == '__main__':
    app2 = create_app()
    app2.run()