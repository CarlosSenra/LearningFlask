class ItemModel:
    def __init__(self):
        self.items = []
    
    def get_all(self):
        return self.items
    
    def add(self, item):
        self.items.append(item)
        return item
    
    def update(self, item_id, data):
        if 0 <= item_id < len(self.items):
            self.items[item_id].update(data)
            return self.items[item_id]
        return None
    
    def delete(self, item_id):
        if 0 <= item_id < len(self.items):
            return self.items.pop(item_id)
        return None

item_model = ItemModel()