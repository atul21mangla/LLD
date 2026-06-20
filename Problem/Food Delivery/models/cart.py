from typing import List, Optional
from models.food_item import FoodItem
from models.restaurant import Restaurant


class Cart:

    def __init__(self):
        self.items: List[FoodItem] = []
        self.restaurant: Optional[Restaurant] = None

    def add_item(self, item: FoodItem):
        self.items.append(item)

    def get_item(self) -> List[FoodItem]:
        return self.items
    
    def get_restaurant(self) -> Optional[Restaurant]:
        return self.restaurant
    
    def set_restaurant(self, restaurant: Restaurant):
        self.restaurant = restaurant

    def get_total_cost(self) -> float:
        return sum(item.price for item in self.items)
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def clear_cart(self):
        self.items.clear()
        self.restaurant = None
