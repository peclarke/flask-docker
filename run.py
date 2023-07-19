from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from flask import abort, redirect

from api import api_blueprint
from utils import clean

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_blueprint)
    return app

APP = create_app()

@APP.route('/')
def index():
    return render_template('index.html')

@APP.errorhandler(404)
def page_not_found(error):
    return render_template('pageNotFound.html'), 404

# Redirecting
@APP.route('/redirectme')
def redirectMe():
    return redirect(url_for('index'))

# LOGGING IN
@APP.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@APP.route('/login', methods=['POST', 'GET'])
def login_auth():
    error=False
    if request.method == "POST":
        user = clean(request.form['username'])
        pss = clean(request.form['password'])

        if 'paul' not in user:
            error=True
            
    return render_template('login.html', error=error)

# Application Starting Routine
if __name__ == "__main__":
    APP.debug = True
    APP.run(host="0.0.0.0", port=8080)