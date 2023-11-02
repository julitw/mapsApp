from flask import Blueprint, render_template
from website.maps.generate_map_Kasia import generate_map_Kasia

map_Kasia_bp = Blueprint('map_Kasia', __name__)


@map_Kasia_bp.route('/map1')
def map_Kasia():
    graph = generate_map_Kasia()

    return render_template('map_Kasia.html', graph=graph)
