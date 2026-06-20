from typing import List, Optional
from models.food_item import FoodItem


class Restaurant:

    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.menu: List[FoodItem] = []

    def add_food_item(self, food_item: FoodItem):
        self.menu.append(food_item)

    def get_menu(self):
        return self.menu

    def get_item_by_code(self, code: str) -> Optional[FoodItem]:
        for item in self.menu:
            if item.get_code() == code:
                return item
        return None
