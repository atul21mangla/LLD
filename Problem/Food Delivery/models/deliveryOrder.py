from models.order import Order

class DeliveryOrder(Order):

    def __init__(self):
        self.__delivery_address = ""

    def set_delivery_address(self, address:str):
        self.__delivery_address = address

    def get_delivery_address(self):
        return self.__delivery_address

    def get_order_type(self)->str:
        return "DELIVERY"
    
