from models.cart import Cart


class User:

    def __init__(self, user_id: str, name: str, address: str):
        self.name = name
        self.user_id = user_id
        self.address = address
        self.cart = Cart()

    def get_cart(self):
        return self.cart
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
