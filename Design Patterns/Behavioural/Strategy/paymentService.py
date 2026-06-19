from abc import ABC, abstractmethod

class PaymentService(ABC):

    @abstractmethod
    def pay(self, amount: float):
        pass

class UPIPayment(PaymentService):

    def __init__(self, upi_id: str):
        self.__upi_id = upi_id

    def pay(self, amount: float):
        print(f"Payment successful through UPI ({self.__upi_id}) for {amount}.")


class CreditCard(PaymentService):

    def __init__(self, card: str):
        self.__card = card

    def pay(self, amount: float):
        print(f"Credit Card payment done for {amount}.")


class ShoppingCart:

    def __init__(self, paymentService: PaymentService):
        self.__paymentService = paymentService

    def changePaymentService(self, paymentService: PaymentService):
        self.__paymentService = paymentService

    def checkout(self, amount: float):
        self.__paymentService.pay(amount)

def main():
    cart = ShoppingCart(UPIPayment("830430@ibl"))
    cart.checkout(800)

    cart.changePaymentService(CreditCard("adf-fsa"))
    cart.checkout(1000)

if __name__ == "__main__":
    main()
    
