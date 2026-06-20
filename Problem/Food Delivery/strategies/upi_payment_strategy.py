from strategies.payment_strategy import PaymentStrategy


class UpiPaymentStrategy(PaymentStrategy):

    def __init__(self, upi_id: str):
        self._upi_id = upi_id

    def pay(self, amount: float) -> bool:
        print(f"Processing UPI payment of Rs.{amount:.2f}")
        print(f"UPI ID: {self._upi_id}")
        print("Payment successful via UPI")
        return True
    
    def get_payment_method(self):
        return "UPI"
