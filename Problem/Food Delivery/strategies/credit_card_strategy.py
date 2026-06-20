from strategies.payment_strategy import PaymentStrategy


class CreditCardPaymentStrategy(PaymentStrategy):
    def __init__(self, card_number: str, expiry: str, cvv: str):
        self.card_number = card_number
        self.expiry = expiry
        self.cvv = cvv
    
    def pay(self, amount: float) -> bool:
        print(f"Processing credit card payment of Rs.{amount:.2f}")
        print(f"Card: ****{self.card_number[-4:]}")
        print(f"Expiry: {self.expiry}")
        print("Payment successful via Credit Card")
        return True
    
    def get_payment_method(self) -> str:
        return "CREDIT_CARD"
