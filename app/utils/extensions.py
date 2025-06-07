from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

auth = HTTPBasicAuth()
db = SQLAlchemy()

@auth.verify_password
def verify_password(username, password):
    from app.models.user import User
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return username