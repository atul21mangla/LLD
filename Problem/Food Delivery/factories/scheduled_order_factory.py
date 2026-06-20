from typing import List
from models.user import User
from models.restaurant import Restaurant
from strategies.payment_strategy import PaymentStrategy
from models.food_item import FoodItem
from models.order import Order

from factories.order_factory import OrderFactory


class ScheduledOrderFactory(OrderFactory):

    def __init__(self, schedule_time: str):
        self._schedule_time = schedule_time

    def create_order(
        self,
        user: User,
        restaurant: Restaurant,
        items: List[FoodItem],
        payment_strategy: PaymentStrategy,
        total_cost: float,
        order_type: str,
    ) -> Order:
        """Creates a scheduled order."""

        order = Order(user, restaurant, items, payment_strategy, total_cost, "SCHEDULED")

        order.schedule_time = self._schedule_time
        print(f"Order scheduled for: {self._schedule_time}")
        return order
