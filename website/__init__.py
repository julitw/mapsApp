from flask import Flask
import os

from website.blueprints.home import home_bp
from website.blueprints.map1 import map1_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(home_bp)
    app.register_blueprint(map1_bp)
    return app
