from app.models.item import item_model

class ItemService:
    @staticmethod
    def get_all_items():
        return item_model.get_all()
    
    @staticmethod
    def create_item(data):
        return item_model.add(data)
    
    @staticmethod
    def update_item(item_id, data):
        return item_model.update(item_id, data)
    
    @staticmethod
    def delete_item(item_id):
        return item_model.delete(item_id)