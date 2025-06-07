from flask import Blueprint, jsonify, request
from app.services.item_service import ItemService

items_bp = Blueprint('items', __name__)

@items_bp.route('/items', methods=['GET'])
def get_items():
    items = ItemService.get_all_items()
    return jsonify(items)

@items_bp.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    item = ItemService.create_item(data)
    return jsonify(item), 201

@items_bp.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = ItemService.update_item(item_id, data)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found."}), 404

@items_bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = ItemService.delete_item(item_id)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found."}), 404