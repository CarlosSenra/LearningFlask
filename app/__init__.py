from flask import Flask
from flasgger import Swagger
from app.utils.extensions import auth, db, jwt
from app.utils.swagger_config import swagger_config, swagger_template
from app.routes import auth_bp, items_bp, register_bp



def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    swagger = Swagger(app, config=swagger_config, template=swagger_template)

    db.init_app(app)
    jwt.init_app(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(items_bp)
    app.register_blueprint(register_bp)
    
    @app.route('/')
    def home():
        """
        Home endpoint
        ---
        responses:
          200:
            description: Welcome message
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Hello, Flask!"
        """
        return "Hello, Flask!"
    
    with app.app_context():
        db.create_all()
    
    return app