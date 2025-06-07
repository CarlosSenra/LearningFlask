from flask import Blueprint, jsonify
from app.utils.extensions import auth

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/hello', methods=['GET'])
@auth.login_required
def hello():
    return jsonify({'message': 'Hello, World!'})