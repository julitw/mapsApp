from flask import Blueprint, render_template
from website.maps.generate_map_Tomek import generate_map_Tomek

map_Tomek_bp = Blueprint('map_Tomek', __name__)


@map_Tomek_bp.route('/map1')
def map_Tomek():
    graph = generate_map_Tomek()

    return render_template('map_Tomek.html', graph=graph)
