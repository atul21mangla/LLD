from typing import List
from models.user import User
from models.restaurant import Restaurant
from strategies.payment_strategy import PaymentStrategy
from models.food_item import FoodItem
from models.order import Order

from factories.order_factory import OrderFactory


class NowOrderFactory(OrderFactory):

    def create_order(
        self,
        user: User,
        restaurant: Restaurant,
        items: List[FoodItem],
        payment_strategy: PaymentStrategy,
        total_cost: float,
        order_type: str,
    ) -> Order:
        """Creates an immediate delivery order."""

        return Order(user, restaurant, items, payment_strategy, total_cost, "NOW_DELIVERY")
