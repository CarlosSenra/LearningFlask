from flask import Blueprint, jsonify, request
from app.services.item_service import ItemService
from app.models.user import User
from app.utils.extensions import db

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register_user():

    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'User alredy exists'}), 400
    
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User createde"}), 201

