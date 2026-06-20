from models.order import Order


class NotificationService:

    @staticmethod
    def notify(order: Order):
        """Send notification for the order"""
        print("\n" + "=" * 50)
        print("NOTIFICATION")
        print("=" * 50)
        print(f"Hey {order.get_user().get_name()}!")
        print(f"Your order of Rs.{order._total:.2f} has been placed successfully!")
        print(f"Order Type: {order._order_type}")
        print(f"Restaurant: {order.get_restaurant().name}")
        print("Items ordered:")
        for item in order._items:
            print(f"  - {item.name} : Rs.{item.price}")
        print(f"Payment Method: {order._payment_strategy.get_payment_method()}")
        print("=" * 50)
        print("You'll receive a confirmation SMS shortly.")
        print("=" * 50 + "\n")
