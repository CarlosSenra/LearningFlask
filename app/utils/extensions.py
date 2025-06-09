from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

auth = HTTPBasicAuth()
db = SQLAlchemy()
jwt = JWTManager()