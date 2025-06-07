from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

# User store (move to database later)
users = {
    "user1": "password1",
    "user2": "password2"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username