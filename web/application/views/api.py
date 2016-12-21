from flask import Blueprint, jsonify


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def api_get_index():
    return jsonify(message='I\'ve got a bad feeling about this...'), 200
