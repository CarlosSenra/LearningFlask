from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

auth = HTTPBasicAuth()
db = SQLAlchemy()
jwt = JWTManager()

@auth.verify_password
def verify_password(username, password):
    from app.models.user import User
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return username