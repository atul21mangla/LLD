from typing import List
from models.user import User
from models.restaurant import Restaurant
from models.food_item import FoodItem
from strategies.payment_strategy import PaymentStrategy


class Order:
    __nextOrderId = 0

    def __init__(
        self,
        user: User,
        restaurant: Restaurant,
        items: List[FoodItem],
        payment_strategy: PaymentStrategy,
        total: float,
        order_type: str,
    ):
        Order.__nextOrderId += 1

        self._order_id = Order.__nextOrderId
        self._user = user
        self._restaurant = restaurant
        self._items = items
        self._payment_strategy = payment_strategy
        self._total = total
        self._order_type = order_type
        self._is_paid = False
        self._status = "PENDING"

    def process_payment(self) -> bool:
        if not self._is_paid:
            self._is_paid = self._payment_strategy.pay(self._total)
            self._status = "PAID"
        return self._is_paid
    
    def get_order_type(self) -> str:
        return self._order_type
    
    def get_total_cost(self) -> float:
        return self._total
    
    def __str__(self):
        return f"Order #{self._order_id} : {self.get_order_type()} - Rs.{self._total} ({self._status})"
    
    def get_user(self) -> User:
        return self._user
    
    def get_restaurant(self) -> Restaurant:
        return self._restaurant
