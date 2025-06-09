from app.models.user import User
from app.utils.extensions import auth, jwt
from flask import g
from flask_jwt_extended import (
    create_access_token,
    jwt_required, 
    get_jwt_identity
)

class UserService:
    @staticmethod
    def create_user(data):
        new_user = User()
        return new_user.register_username(data)
    
    @staticmethod
    @auth.verify_password
    def verify_password(username, password):
        from app.models.user import User
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            g.current_user = user
            return True
        return False
    
    @staticmethod
    def create_token_for_user(user):
        return create_access_token(identity=str(user.id))
    
    @staticmethod
    @jwt_required
    def get_current_user_from_token():
        user_id = get_jwt_identity()
        return User.query.get(user_id)