from typing import List
from models.order import Order


class OrderManager:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._initialized = False
        return cls.__instance

    def __init__(self):
        if hasattr(self, "_initialized") and not self._initialized:
            self._orders: List[Order] = []
            self._initialized = True

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def add_order(self, order: Order):
        self._orders.append(order)

    def get_all_orders(self) -> List[Order]:
        return self._orders

    def get_orders_by_user(self, user_id: int) -> List[Order]:
        return [order for order in self._orders if order.get_user().user_id == user_id]
