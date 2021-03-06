from os import environ
from . import apply_blueprint
from .oauth import apply_oauth_blueprint
from .odes import apply_odes_blueprint
from .redirect import apply_redirect_blueprint
from flask import Flask

# import logging
# import sys

def make_app(url_prefix):
    static_url_path = '{}/static'.format(url_prefix or '')
    app = Flask(__name__, static_url_path=static_url_path)
    apply_blueprint(app, url_prefix)
    apply_oauth_blueprint(app, url_prefix)
    apply_odes_blueprint(app, url_prefix)
    apply_redirect_blueprint(app)

    app.config['SESSION_COOKIE_PATH'] = url_prefix
    app.config['SESSION_COOKIE_NAME'] = 'metro-extracts-session'

    # app.logger.addHandler(logging.StreamHandler(sys.stdout))
    # app.logger.setLevel(logging.DEBUG)

    return app

app = make_app(environ.get('URL_PREFIX'))
