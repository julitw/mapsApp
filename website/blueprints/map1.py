from flask import Blueprint, render_template

# map1_bp = Blueprint('map1', __name__)

# @map1_bp.route('/map1')
# def map1():
#     return render_template('map1.html')

from flask import render_template
from website.maps.generate_map1 import  generate_map1

map1_bp = Blueprint('map1', __name__)

@map1_bp.route('/map1')
def map1():
    graph = generate_map1()

    return render_template('map1.html', graph=graph)
