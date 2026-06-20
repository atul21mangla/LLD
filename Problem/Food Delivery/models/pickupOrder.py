from models.order import Order

class PickupOrder(Order):

    def __init__(self):
        self.__restaurant_address = ""

    def set_restaurant_address(self, address:str):
        self.__restaurant_address = address

    def get_restaurant_address(self):
        return self.__restaurant_address

    def get_order_type(self)->str:
        return "PICKUP"
    
