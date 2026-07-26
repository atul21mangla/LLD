from abc import ABC, abstractmethod


class BasePizza(ABC):

    @abstractmethod
    def getCost(self) -> int:
        pass

    @abstractmethod
    def getDescription(self) -> str:
        pass


class MargheritaPizza(BasePizza):

    def getCost(self) -> int:
        return 100

    def getDescription(self) -> str:
        return "Margherita Pizza"


class PaneerPizza(BasePizza):

    def getCost(self) -> int:
        return 150

    def getDescription(self) -> str:
        return "Paneer Pizza"


# Base Decorator delegates default behavior to the wrapped pizza
class PizzaDecorator(BasePizza):

    def __init__(self, pizza: BasePizza):
        self._pizza = pizza

    def getCost(self) -> int:
        return self._pizza.getCost()

    def getDescription(self) -> str:
        return self._pizza.getDescription()


# Concrete Decorators override only what they modify
class ExtraCheese(PizzaDecorator):

    def getCost(self) -> int:
        return super().getCost() + 20

    def getDescription(self) -> str:
        return f"{super().getDescription()} with Extra Cheese"


class Mushroom(PizzaDecorator):

    def getCost(self) -> int:
        return super().getCost() + 10

    def getDescription(self) -> str:
        return f"{super().getDescription()} with Mushroom"


def main():
    pizza: BasePizza = Mushroom(ExtraCheese(PaneerPizza()))

    print(f"Order: {pizza.getDescription()}")
    print(f"Total Cost: ₹{pizza.getCost()}")


if __name__ == "__main__":
    main()