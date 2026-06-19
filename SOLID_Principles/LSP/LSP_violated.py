"""
LISKOV SUBSTITUTION PRINCIPLE - VIOLATED
Child classes should be substitutable for their parent classes without breaking functionality
"""

from abc import ABC, abstractmethod

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


# Base class
class PaymentProcessor(ABC):
    """Base payment processor - defines contract for all payment methods"""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Process payment for given amount"""
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str) -> bool:
        """Refund a previous payment"""
        pass
    
    @abstractmethod
    def get_balance(self) -> float:
        """Get available balance"""
        pass


# LSP VIOLATION 1: CreditCardPayment changes the expected behavior
class CreditCardPayment(PaymentProcessor):
    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number
        self.cvv = cvv
        self.transactions = []
        self.balance = 10000  # Credit limit
    
    def process_payment(self, amount: float) -> bool:
        if amount <= self.balance:
            self.balance -= amount
            transaction_id = f"CC_{len(self.transactions)}"
            self.transactions.append(transaction_id)
            print(f"Credit Card: Processed Rs {amount}. Remaining limit: Rs {self.balance}")
            return True
        else:
            print(f"Credit Card: Insufficient credit limit!")
            return False
    
    def refund_payment(self, transaction_id: str) -> bool:
        # Works as expected
        print(f"Credit Card: Refunded transaction {transaction_id}")
        return True
    
    def get_balance(self) -> float:
        return self.balance


# LSP VIOLATION 2: CashPayment violates LSP - Cash doesn't support refunds!
class CashPayment(PaymentProcessor):
    def __init__(self):
        self.transactions = []
        self.cash_available = 5000
    
    def process_payment(self, amount: float) -> bool:
        if amount <= self.cash_available:
            self.cash_available -= amount
            transaction_id = f"CASH_{len(self.transactions)}"
            self.transactions.append(transaction_id)
            print(f"Cash: Paid Rs {amount}. Remaining cash: Rs {self.cash_available}")
            return True
        else:
            print(f"Cash: Insufficient cash!")
            return False
    
    # VIOLATION: Cash payments cannot be refunded!
    def refund_payment(self, transaction_id: str) -> bool:
        # Throws exception instead of working properly
        raise NotImplementedError("Cash payments cannot be refunded!")
    
    def get_balance(self) -> float:
        return self.cash_available


# LSP VIOLATION 3: CryptoPayment changes return type behavior
class CryptoPayment(PaymentProcessor):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address
        self.transactions = []
        self.balance = 2.5  # BTC
    
    def process_payment(self, amount: float) -> bool:
        # VIOLATION: Changes meaning - amount is in INR but balance is in BTC
        btc_amount = amount / 5000000  # Assume 1 BTC = 50L INR
        if btc_amount <= self.balance:
            self.balance -= btc_amount
            transaction_id = f"CRYPTO_{len(self.transactions)}"
            self.transactions.append(transaction_id)
            print(f"Crypto: Paid {btc_amount} BTC (Rs {amount})")
            return True
        else:
            print(f"Crypto: Insufficient balance!")
            return False
    
    def refund_payment(self, transaction_id: str) -> bool:
        print(f"Crypto: Refunded transaction {transaction_id}")
        return True
    
    def get_balance(self) -> float:
        # VIOLATION: Returns BTC, not INR like other classes!
        return self.balance  # Should return INR for consistency


# ShoppingCart that uses PaymentProcessor
class ShoppingCart:
    def __init__(self):
        self._items = []
    
    def add_item(self, product: Product):
        self._items.append(product)
    
    def calculate_total(self) -> float:
        return sum(item.price for item in self._items)
    
    def checkout(self, payment_processor: PaymentProcessor) -> bool:
        """Checkout using any payment processor"""
        total = self.calculate_total()
        print(f"\nTotal amount to pay: Rs {total}")
        
        # Process payment
        success = payment_processor.process_payment(total)
        
        if success:
            print("Payment successful!")
            # Assume we get a transaction ID
            transaction_id = "TXN123"
            
            # Later, we might want to refund
            # This will FAIL for CashPayment!
            payment_processor.refund_payment(transaction_id)
        else:
            print("Payment failed!")
        
        return success


# Demonstration of LSP violations
if __name__ == "__main__":
    # Create cart
    cart = ShoppingCart()
    cart.add_item(Product("Laptop", 50000))
    cart.add_item(Product("Mouse", 2000))
    
    print("=== LISKOV SUBSTITUTION PRINCIPLE - VIOLATIONS ===\n")
    
    # Test with CreditCard - Works fine
    print("1. Using Credit Card Payment:")
    cc_payment = CreditCardPayment("1234-5678", "123")
    cart.checkout(cc_payment)
    
    # Test with Cash - VIOLATION: This will crash!
    print("\n2. Using Cash Payment (VIOLATION):")
    cash_payment = CashPayment()
    try:
        cart.checkout(cash_payment)
    except NotImplementedError as e:
        print(f"❌ ERROR: {e}")
        print("   CashPayment broke LSP - cannot be substituted for PaymentProcessor!")
    
    # Test with Crypto - VIOLATION: Different behavior
    print("\n3. Using Crypto Payment (VIOLATION):")
    crypto_payment = CryptoPayment("1A2B3C4D")
    cart.checkout(crypto_payment)
    
    print("\n❌ PROBLEMS IDENTIFIED:")
    print("   1. CashPayment doesn't support refunds (throws exception)")
    print("   2. CryptoPayment returns balance in different currency")
    print("   3. Client expecting refund capability breaks with CashPayment")