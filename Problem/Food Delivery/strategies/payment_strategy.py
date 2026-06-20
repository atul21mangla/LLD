from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self,amount:float) ->bool:
        """Process payment and retyrn success status"""
        pass

    @abstractmethod
    def get_payment_method(self) -> str:
        """Return payment method name"""
        pass