from flask import Blueprint, jsonify, request
from app.services.user_service import UserService
from app.utils.extensions import db

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register_user():
    """Registre um usuario

    Returns:
        _type_: _description_
    """
    data = request.get_json()
    UserService.create_user(data)

    return jsonify({"msg": "User createde"}), 201

