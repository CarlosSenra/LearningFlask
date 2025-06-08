from app.models.user import User

class UserService:
    @staticmethod
    def create_user(data):
        new_user = User()
        return new_user.register_username(data)