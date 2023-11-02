from flask import Blueprint, render_template
from website.maps.generate_map_Marcysia import generate_map_Marcysia

map_Marcysia_bp = Blueprint('map_Marcysia', __name__)


@map_Marcysia_bp.route('/map_Marcysia')
def map_Marcysia():
    graph = generate_map_Marcysia()

    return render_template('map_Marcysia.html', graph=graph)
