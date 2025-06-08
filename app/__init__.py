from flask import Flask
from flasgger import Swagger
from app.utils.extensions import auth, db
from app.routes import auth_bp, items_bp, register_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    db.init_app(app)
    Swagger(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(items_bp)
    app.register_blueprint(register_bp)
    
    @app.route('/')
    def home():
        return "Hello, Flask!"
    
    with app.app_context():
        db.create_all()
    
    return app