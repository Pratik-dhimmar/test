# sweet_shop/sweet_shop_manager.py
class SweetShopManager:
    def __init__(self):
        self.sweets = [] # Initialize an empty list to store sweets

    def add_sweet(self, id, name, category, price, quantity):
        # Check for unique ID (optional but good practice)
        for sweet in self.sweets:
            if sweet['id'] == id:
                raise ValueError("Sweet with this ID already exists.")
        sweet = {
            'id': id,
            'name': name,
            'category': category,
            'price': price,
            'quantity': quantity
        }
        self.sweets.append(sweet)

    def view_sweets(self):
        return self.sweets
    
    # sweet_shop/sweet_shop_manager.py (continued)
    def delete_sweet(self, sweet_id):
        initial_len = len(self.sweets)
        self.sweets = [sweet for sweet in self.sweets if sweet['id'] != sweet_id]
        if len(self.sweets) == initial_len:
            raise ValueError(f"Sweet with ID {sweet_id} not found.")