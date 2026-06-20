from abc import ABC, abstractmethod
from typing import List
from models.user import User
from models.restaurant import Restaurant
from strategies.payment_strategy import PaymentStrategy
from models.food_item import FoodItem
from models.order import Order


class OrderFactory(ABC):

    @abstractmethod
    def create_order(
        self,
        user: User,
        restaurant: Restaurant,
        items: List[FoodItem],
        payment_strategy: PaymentStrategy,
        total_cost: float,
        order_type: str,
    ) -> Order:
        """Create and return an order."""
        pass
