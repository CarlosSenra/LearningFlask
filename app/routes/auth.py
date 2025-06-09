from flask import Blueprint, jsonify, g
from app.utils.extensions import auth
from app.services.user_service import UserService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
@auth.login_required
def hello():
    token = UserService.create_token_for_user(g.current_user)
    return jsonify({'token': token, 'msg':'Login successful'})

@auth_bp.route('/protected', methods=['GET'])
@auth.login_required
def protected():
    return jsonify({'message': f'Hello {g.current_user.username}!', 'user_id': g.current_user.id})

@auth_bp.route('/test', methods=['GET'])
def test():
    """Test route to verify blueprint registration"""
    return jsonify({'message': 'Auth blueprint is working!'})