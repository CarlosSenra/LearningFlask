from app.utils.extensions import db
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash,password)
    
    @classmethod
    def register_username(cls, data):
        if cls.query.filter_by(username=data['username']).first():
            return jsonify({'error': 'User alredy exists'}), 400
    
        try:
            new_user = cls(username=data['username'])
            new_user.set_password(data['password'])
            db.session.add(new_user)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            return None, {'error': 'Failed to create user'}
    
    def __repr__(self):
        return f'<User {self.username}>'