from typing import List, Optional
from models.user import User
from models.restaurant import Restaurant
from models.food_item import FoodItem
from models.order import Order
from models.cart import Cart
from managers.restaurant_manager import RestaurantManager
from managers.orderManager import OrderManager
from services.notification_service import NotificationService
from strategies.payment_strategy import PaymentStrategy
from factories.order_factory import OrderFactory
from factories.now_order_factory import NowOrderFactory
from factories.scheduled_order_factory import ScheduledOrderFactory



class TomatoApp:

    def __init__(self):
        self._restaurant_manager = RestaurantManager.get_instance()
        self._initialize_restaurants()


    def _initialize_restaurants(self):
        """Initialize restaurants with food items"""

        restaurant1 = Restaurant("Haldirams", "Delhi")
        restaurant1.add_food_item(FoodItem("P1", "Raj Kachori", 80))
        restaurant1.add_food_item(FoodItem("P2", "Cham Cham", 50))
        restaurant1.add_food_item(FoodItem("P3", "Chole Bhature", 100))


        restaurant2 = Restaurant("Punjabi Anghiti", "Banglore")
        restaurant2.add_food_item(FoodItem("P1", "Paneer Butter masala", 250))
        restaurant2.add_food_item(FoodItem("P2", "Noodles", 150))
        restaurant2.add_food_item(FoodItem("P3", "Malai Chaap", 180))


        restaurant3 = Restaurant("Starbucks", "Pune")
        restaurant3.add_food_item(FoodItem("P1", "Cappuccino", 200))
        restaurant3.add_food_item(FoodItem("P2", "Latte", 250))


        self._restaurant_manager.add_restaurant(restaurant1)
        self._restaurant_manager.add_restaurant(restaurant2)
        self._restaurant_manager.add_restaurant(restaurant3)

    
    def search_restaurant(self, location:str) -> List[Restaurant]:
        return self._restaurant_manager.search_by_location(location)
    

    def select_restaurant(self, user:User, restaurant:Restaurant):
        """Select a restaurant for user's cart."""

        cart = user.get_cart()
        cart.set_restaurant(restaurant)

    
    def add_to_cart(self, item_code:str, user:User):
        """Add item to user's cart"""

        cart = user.get_cart()
        
        restaurant = cart.get_restaurant()

        if restaurant is None:
            print("Please select a restaurant first.")
            return
        
        # Find item by code
        food_item = restaurant.get_item_by_code(item_code)

        if food_item is not None:
            cart.add_item(food_item)
            print(f"\nItem {food_item.name} added to cart.")

        
    def checkout_now(self,user:User, order_type:str, 
                     payment_strategy:PaymentStrategy) -> Optional[Order]:
        
        """Checkout Immediately"""

        return self.checkout(user,order_type,payment_strategy, NowOrderFactory())


    def checkout_scheduled(self, user: User, order_type: str, 
                          payment_strategy: PaymentStrategy, 
                          schedule_time: str) -> Optional[Order]:
        """Checkout with scheduling"""
        return self.checkout(user, order_type, payment_strategy, 
                           ScheduledOrderFactory(schedule_time))
    

    def checkout(self,user:User, order_type:str, payment_strategy:PaymentStrategy, 
                 order_factory:OrderFactory) -> Optional[Order]:
        """Common checkout method"""

        cart = user.get_cart()

        if cart.is_empty():
            print("Cart is empty. Please add items to cart before checkout.")
            return None

        restaurant = cart.get_restaurant()
        items_ordered = cart.get_item()
        total_cost = cart.get_total_cost()


        order = order_factory.create_order(user, restaurant, items_ordered, 
                                           payment_strategy, total_cost, order_type)

        OrderManager.get_instance().add_order(order)
        print(f"\n Order created successfully.")
        return order
    

    def pay_for_order(self, user:User, order:Order):
        """ Process payment for thr order."""
    
        is_payment_success = order.process_payment()

        if is_payment_success:
            # Send Notification
            NotificationService.notify(order)

            # Clear the cart
            user.get_cart().clear_cart()
            print("Cart Cleared after successful payment.")

        else:
            print("Payment Failed.")

    
    def print_user_cart(self,user:User):
        """Print user's cart content"""

        print("\nItems in Cart.....")
        print("-" * 40)
        items = user.get_cart().get_item()

        for item in items:
            print(f"{item.get_code()}: {item.name} - {item.price}")

        print("-" *40)
        print(f"Grand Total : RS. {user.get_cart().get_total_cost():.2f}")
        print("-" * 40)




