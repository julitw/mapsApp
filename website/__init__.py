from flask import Flask
import os

from website.blueprints.home import home_bp
from website.blueprints.map1 import map1_bp
from website.blueprints.map_Kasia import map_Kasia_bp
from website.blueprints.map_Tomek import map_Tomek_bp
from website.blueprints.map_Gabrysia import map_Gabrysia_bp
from website.blueprints.map_Marcysia import map_Marcysia_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(home_bp)
    app.register_blueprint(map1_bp)
    app.register_blueprint(map_Kasia_bp)
    app.register_blueprint(map_Tomek_bp)
    app.register_blueprint(map_Gabrysia_bp)
    app.register_blueprint(map_Marcysia_bp)
    return app
