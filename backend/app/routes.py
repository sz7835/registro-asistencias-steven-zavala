from flask import Blueprint, jsonify

example_bp = Blueprint('example', __name__)

@example_bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})
