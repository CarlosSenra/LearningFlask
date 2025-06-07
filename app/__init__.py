from flask import Flask
from flasgger import Swagger
from app.utils.extensions import auth
from app.routes import auth_bp, items_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    Swagger(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(items_bp)
    
    @app.route('/')
    def home():
        return "Hello, Flask!"
    
    return app