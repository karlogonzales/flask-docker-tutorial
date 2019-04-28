from flask import jsonify, Blueprint


bp = Blueprint('sample', __name__, url_prefix='/')


@bp.route("", methods={'GET'})
def get_sample():
    return jsonify({'message': 'Hello World'})



