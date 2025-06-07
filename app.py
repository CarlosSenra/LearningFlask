from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger

app = Flask(__name__)

auth = HTTPBasicAuth()

users = {"user1": "password1",
        "user2": "password2"}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

@app.route('/')
def home():
    return "Hello, Flask!"

itens = []

@app.route('/itens', methods=['GET'])
def get_items():
    return jsonify(itens)


@app.route('/itens', methods=['POST'])
def create_item():
    data = request.get_json()
    itens.append(data)
    return jsonify(data), 201

@app.route('/itens/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    if 0 <= item_id < len(itens):
        itens[item_id].update(data)
        return jsonify(itens[item_id])
    return jsonify({"error": "Item not found."}), 404
    
@app.route('/itens/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(itens):
        removed = itens.pop(item_id)
        return jsonify(removed)
    return jsonify({"error": "Item not found."}), 404

@app.route('/hello', methods=['GET'])
@auth.login_required
def hello():
    return jsonify({'message': 'Hello, World!'})

app.config['SWAGGER'] = {
    'title': 'My Flask API',
    'uiversion': 3
}

swagger = Swagger(app)

if __name__ == "__main__":
    app.run(debug=True)
    
    