# backend/app/routes.py

from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/ping')
def ping():
    return jsonify({'message': 'pong'})
