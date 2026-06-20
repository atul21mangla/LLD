from tomato_app import TomatoApp
from models.user import User
from strategies.upi_payment_strategy import UpiPaymentStrategy

def main():
    # Simulating a happy flow
    # Create TomatoApp Object
    tomato = TomatoApp()
    
    # Simulate a user coming in (Happy Flow)
    user = User(101, "Aditya", "Delhi")
    print(f"User: {user.get_name()} is active.\n")
    
    # User searches for restaurants by location
    restaurant_list = tomato.search_restaurant("Delhi")
    
    if not restaurant_list:
        print("No restaurants found!")
        return
    
    print("Found Restaurants:")
    for restaurant in restaurant_list:
        print(f" - {restaurant.name}")
    
    print()
    
    # User selects a restaurant
    selected_restaurant = restaurant_list[0]
    tomato.select_restaurant(user, selected_restaurant)
    print(f"Selected restaurant: {selected_restaurant.name}\n")
    
    # Checking all food items for restaurant
    menu_items = selected_restaurant.get_menu()
    for item in menu_items:
        print(f"{item.get_code()}: {item.name} - {item.price}")

    # User adds items to the cart
    tomato.add_to_cart("P1", user)
    tomato.add_to_cart("P2", user)
    
    # Print user's cart
    tomato.print_user_cart(user)
    
    # User checkout the cart
    order = tomato.checkout_now(user, "Delivery", UpiPaymentStrategy("1234567890@upi"))
    
    # User pays for the cart. If payment is successful, notification is sent.
    if order:
        tomato.pay_for_order(user, order)

if __name__ == "__main__":
    main()
