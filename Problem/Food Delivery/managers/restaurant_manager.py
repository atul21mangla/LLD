from typing import List
from models.restaurant import Restaurant


class RestaurantManager:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.initialized = False
        return cls.__instance

    def __init__(self):
        if hasattr(self, "_initialized") and self._initialized:
            return

        self.restaurants: List[Restaurant] = []
        self._initialized = True

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def add_restaurant(self, restaurant: Restaurant):
        self.restaurants.append(restaurant)

    def get_all_restaurants(self) -> List[Restaurant]:
        return self.restaurants

    def search_by_location(self, location: str):
        return [r for r in self.restaurants if r.location.lower() == location.lower()]

    def search_by_name(self, name: str):
        for r in self.restaurants:
            if r.name.lower() == name.lower():
                return r
        return None
