from flask import Blueprint
api_blueprint = Blueprint('api', __name__, template_folder='templates')

# You can output API in json form
@api_blueprint.route('/api')
def api():
    res = {
        0: 'Pablo',
        1: 'James',
        2: 'Barack Obama'
    }
    return res