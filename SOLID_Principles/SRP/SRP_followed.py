"""
SRP Compliant Example:
Each class now has a single responsibility:
1. ShoppingCart - Manages cart items and calculates total
2. ShoppingCartPrinter - Handles invoice printing
3. ShoppingCartStorage - Handles database operations
"""

# Product class representing any item in eCommerce
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


# 1. ShoppingCart: Only responsible for Cart related business logic
class ShoppingCart:
    def __init__(self):
        self._products = []  # Store products (no need for heap allocation in Python)
    
    def add_product(self, product: Product):
        """Add product to cart"""
        self._products.append(product)
    
    def get_products(self):
        """Get all products in cart"""
        return self._products.copy()  # Return copy to prevent external modification
    
    def calculate_total(self) -> float:
        """Calculate total price in cart"""
        total = 0
        for product in self._products:
            total += product.price
        return total


# 2. ShoppingCartPrinter: Only responsible for printing invoices
class ShoppingCartPrinter:
    def __init__(self, cart: ShoppingCart):
        self._cart = cart
    
    def print_invoice(self):
        """Print invoice for the shopping cart"""
        print("Shopping Cart Invoice:")
        for product in self._cart.get_products():
            print(f"{product.name} - Rs {product.price}")
        print(f"Total: Rs {self._cart.calculate_total()}")


# 3. ShoppingCartStorage: Only responsible for saving cart to DB
class ShoppingCartStorage:
    def __init__(self, cart: ShoppingCart):
        self._cart = cart
    
    def save_to_database(self):
        """Save shopping cart to database"""
        print("Saving shopping cart to database...")
        # Database saving logic would go here


# Main execution
if __name__ == "__main__":
    # Create shopping cart
    cart = ShoppingCart()
    
    # Add products (no need for 'new' keyword - Python handles memory automatically)
    laptop = Product("Laptop", 50000)
    mouse = Product("Mouse", 2000)
    
    cart.add_product(laptop)
    cart.add_product(mouse)
    
    # Print invoice using printer class
    printer = ShoppingCartPrinter(cart)
    printer.print_invoice()
    
    # Save to database using storage class
    db_storage = ShoppingCartStorage(cart)
    db_storage.save_to_database()
    
    # No need for manual cleanup - Python's garbage collector handles it