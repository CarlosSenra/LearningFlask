from app import create_app
from app.utils.extensions import db
from app.models.user import User

app = create_app()

with app.app_context():
    # Criar usuários de teste
    user1 = User(username='user1')
    user1.set_password('password1')
    
    user2 = User(username='user2')
    user2.set_password('password2')
    
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    
    print("Usuários criados!")