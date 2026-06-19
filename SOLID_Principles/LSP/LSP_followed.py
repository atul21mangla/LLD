"""
CORRECTED: Following BOTH SRP and LSP
Separate interfaces for separate responsibilities
"""

from abc import ABC, abstractmethod
from typing import Optional, List
from datetime import datetime

# Product and ShoppingCart (same as before)
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self._items = []
    
    def add_item(self, product: Product):
        self._items.append(product)
    
    def calculate_total(self) -> float:
        return sum(item.price for item in self._items)


# ===== SEPARATE INTERFACES FOR SEPARATE RESPONSIBILITIES =====

# Responsibility 1: Payment Processing
class PaymentProcessor(ABC):
    """Only responsible for processing payments"""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Process a payment"""
        pass
    
    @abstractmethod
    def get_payment_method_name(self) -> str:
        """Return name of payment method"""
        pass


# Responsibility 2: Refund Handling (Separate interface)
class RefundHandler(ABC):
    """Only responsible for handling refunds"""
    
    @abstractmethod
    def can_refund(self) -> bool:
        """Check if refund is supported"""
        pass
    
    @abstractmethod
    def process_refund(self, transaction_id: str, amount: float) -> bool:
        """Process a refund"""
        pass


# Responsibility 3: Balance Inquiry (Separate interface)
class BalanceInquiry(ABC):
    """Only responsible for balance checking"""
    
    @abstractmethod
    def get_balance(self) -> float:
        """Get current balance"""
        pass
    
    @abstractmethod
    def get_currency(self) -> str:
        """Get currency of balance"""
        pass


# ===== CONCRETE IMPLEMENTATIONS =====

# 1. Credit Card - Supports all features but keeps them separate
class CreditCardPayment(PaymentProcessor, RefundHandler, BalanceInquiry):
    """Credit Card implementation - supports payment, refund, and balance inquiry"""
    
    def __init__(self, card_number: str, cvv: str, credit_limit: float = 100000):
        self.card_number = card_number
        self.cvv = cvv
        self.credit_limit = credit_limit
        self.used_credit = 0
        self.transactions = {}
    
    # PaymentProcessor methods
    def process_payment(self, amount: float) -> bool:
        if self.used_credit + amount <= self.credit_limit:
            self.used_credit += amount
            transaction_id = f"CC_{len(self.transactions)}"
            self.transactions[transaction_id] = amount
            print(f"💳 Credit Card: Processed Rs {amount}")
            return True
        print(f"❌ Credit Card: Insufficient credit limit!")
        return False
    
    def get_payment_method_name(self) -> str:
        return "Credit Card"
    
    # RefundHandler methods
    def can_refund(self) -> bool:
        return True
    
    def process_refund(self, transaction_id: str, amount: float) -> bool:
        if transaction_id in self.transactions:
            refunded_amount = self.transactions[transaction_id]
            self.used_credit -= refunded_amount
            del self.transactions[transaction_id]
            print(f"💳 Credit Card: Refunded Rs {refunded_amount}")
            return True
        print(f"❌ Credit Card: Transaction {transaction_id} not found")
        return False
    
    # BalanceInquiry methods
    def get_balance(self) -> float:
        return self.credit_limit - self.used_credit
    
    def get_currency(self) -> str:
        return "INR"


# 2. Cash Payment - Only supports payment (no refund, no balance)
class CashPayment(PaymentProcessor):
    """Cash payment - only supports payment, nothing else"""
    
    def __init__(self, cash_on_hand: float = 5000):
        self.cash_on_hand = cash_on_hand
        self._payment_made = False
    
    # PaymentProcessor methods only
    def process_payment(self, amount: float) -> bool:
        if amount <= self.cash_on_hand:
            self.cash_on_hand -= amount
            self._payment_made = True
            print(f"💵 Cash: Paid Rs {amount}. Remaining cash: Rs {self.cash_on_hand}")
            return True
        print(f"❌ Cash: Insufficient cash!")
        return False
    
    def get_payment_method_name(self) -> str:
        return "Cash"
    
    # No refund methods - this class doesn't implement RefundHandler
    # No balance methods - this class doesn't implement BalanceInquiry


# 3. UPI - Supports payment and balance, but not refund (in this version)
class UPIPayment(PaymentProcessor, BalanceInquiry):
    """UPI payment - supports payment and balance inquiry, but not refund"""
    
    def __init__(self, upi_id: str, bank_balance: float = 50000):
        self.upi_id = upi_id
        self.bank_balance = bank_balance
        self.transaction_id = None
    
    # PaymentProcessor methods
    def process_payment(self, amount: float) -> bool:
        if amount <= self.bank_balance:
            self.bank_balance -= amount
            self.transaction_id = f"UPI_{datetime.now().timestamp()}"
            print(f"📱 UPI: Paid Rs {amount} from {self.upi_id}")
            return True
        print(f"❌ UPI: Insufficient balance!")
        return False
    
    def get_payment_method_name(self) -> str:
        return "UPI"
    
    # BalanceInquiry methods
    def get_balance(self) -> float:
        return self.bank_balance
    
    def get_currency(self) -> str:
        return "INR"
    
    # No refund methods - intentionally not supported


# 4. Fixed Term Account (from your bank example) - Only deposit, no withdrawal
class FixedTermAccount(PaymentProcessor):
    """Fixed term account - only supports deposit, withdrawal not allowed"""
    
    def __init__(self, account_number: str, term_months: int = 12):
        self.account_number = account_number
        self.term_months = term_months
        self.balance = 0
        self.deposits = []
    
    def process_payment(self, amount: float) -> bool:
        """In fixed term account, 'payment' means deposit"""
        self.balance += amount
        self.deposits.append({
            'amount': amount,
            'date': datetime.now(),
            'maturity_date': datetime.now().replace(year=datetime.now().year + 1)
        })
        print(f"🏦 Fixed Term Account: Deposited Rs {amount}. New balance: Rs {self.balance}")
        print(f"   ⚠️  Note: Withdrawal allowed only after {self.term_months} months")
        return True
    
    def get_payment_method_name(self) -> str:
        return f"Fixed Term Account ({self.term_months} months)"
    
    # No withdraw method - that's by design for fixed term accounts!


# ===== CLIENT CODE THAT RESPECTS BOTH SRP AND LSP =====

class CheckoutService:
    """Only responsible for checkout/payment processing"""
    
    def __init__(self, payment_processor: PaymentProcessor):
        self._payment_processor = payment_processor
    
    def process_checkout(self, cart: ShoppingCart) -> bool:
        """Process checkout using the payment processor"""
        total = cart.calculate_total()
        print(f"\n💰 Total amount: Rs {total}")
        print(f"💳 Payment method: {self._payment_processor.get_payment_method_name()}")
        
        success = self._payment_processor.process_payment(total)
        
        if success:
            print("✅ Checkout successful!")
        else:
            print("❌ Checkout failed!")
        
        return success


class RefundService:
    """Separate class responsible ONLY for refunds"""
    
    def __init__(self, refund_handler: RefundHandler):
        self._refund_handler = refund_handler
    
    def process_refund(self, transaction_id: str, amount: float) -> bool:
        """Process refund if supported"""
        if not self._refund_handler.can_refund():
            print(f"❌ Refunds not supported by this payment method")
            return False
        
        print(f"\n🔄 Processing refund for transaction: {transaction_id}")
        return self._refund_handler.process_refund(transaction_id, amount)


class BalanceService:
    """Separate class responsible ONLY for balance inquiries"""
    
    def __init__(self, balance_inquiry: BalanceInquiry):
        self._balance_inquiry = balance_inquiry
    
    def show_balance(self) -> None:
        """Display current balance"""
        balance = self._balance_inquiry.get_balance()
        currency = self._balance_inquiry.get_currency()
        print(f"💰 Current balance: {currency} {balance}")


# ===== DEMONSTRATION =====

if __name__ == "__main__":
    # Create shopping cart
    cart = ShoppingCart()
    cart.add_item(Product("Laptop", 50000))
    cart.add_item(Product("Mouse", 2000))
    
    print("="*60)
    print("SRP + LSP COMPLIANT PAYMENT SYSTEM")
    print("="*60)
    
    # Test 1: Credit Card (supports all features)
    print("\n1️⃣ CREDIT CARD PAYMENT")
    print("-" * 40)
    cc_payment = CreditCardPayment("1234-5678-9012-3456", "123")
    
    # Each service uses only the interfaces it needs
    checkout_service = CheckoutService(cc_payment)
    checkout_service.process_checkout(cart)
    
    refund_service = RefundService(cc_payment)
    refund_service.process_refund("CC_0", 50000)
    
    balance_service = BalanceService(cc_payment)
    balance_service.show_balance()
    
    # Test 2: Cash Payment (only payment, no refund/balance)
    print("\n2️⃣ CASH PAYMENT")
    print("-" * 40)
    cash_payment = CashPayment(100000)
    
    checkout_service2 = CheckoutService(cash_payment)
    checkout_service2.process_checkout(cart)
    
    # This won't work - Cash doesn't implement RefundHandler
    # refund_service2 = RefundService(cash_payment)  # Type error!
    print("ℹ️  Cash doesn't support refunds or balance inquiry - that's fine!")
    
    # Test 3: Fixed Term Account (only deposits)
    print("\n3️⃣ FIXED TERM ACCOUNT")
    print("-" * 40)
    fixed_account = FixedTermAccount("FIX12345", 12)
    
    checkout_service3 = CheckoutService(fixed_account)
    checkout_service3.process_checkout(cart)
    
    print("\n" + "="*60)
    print("✅ BENEFITS OF THIS DESIGN:")
    print("="*60)
    print("1. SRP: Each class has ONE reason to change")
    print("   - PaymentProcessor: Only payment logic")
    print("   - RefundHandler: Only refund logic")
    print("   - BalanceInquiry: Only balance logic")
    print("\n2. LSP: Subclasses are truly substitutable")
    print("   - CashPayment works wherever PaymentProcessor is expected")
    print("   - FixedTermAccount works without throwing unexpected exceptions")
    print("\n3. Interface Segregation: Clients depend only on what they need")
    print("   - CheckoutService only needs PaymentProcessor")
    print("   - RefundService only needs RefundHandler")
    print("   - BalanceService only needs BalanceInquiry")