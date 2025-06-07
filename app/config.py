class Config:
    
    SECRET_KEY = 'my_secret_key'
    CACHE_TYPE = 'simple'
    SWAGGER = {
        'title': 'Goutmet Recipes Catalog',
        'universion': 3
    }
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'my_secret_key_jwt'