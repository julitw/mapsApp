from flask import Blueprint, render_template
from website.maps.generate_map_Gabrysia import generate_map_Gabrysia

map_Gabrysia_bp = Blueprint('map_Gabrysia', __name__)


@map_Gabrysia_bp.route('/map1')
def map_Gabrysia():
    graph = generate_map_Gabrysia()

    return render_template('map_Gabrysia.html', graph=graph)
