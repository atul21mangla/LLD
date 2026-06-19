"""
SRP Violation Example:
The ShoppingCart class has multiple responsibilities:
1. Managing cart items
2. Calculating total
3. Printing invoices
4. Saving to database
"""

# Product class representing any item of any ECommerce
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


# Violating SRP: ShoppingCart is handling multiple responsibilities
class ShoppingCart:
    def __init__(self):
        self._products = []  # Using single underscore for "protected" (Python convention)
    
    def add_product(self, product: Product):
        """Add product to cart"""
        self._products.append(product)
    
    def get_products(self):
        """Get all products in cart"""
        return self._products.copy()  # Return a copy to prevent external modification
    
    # Responsibility 1: Calculates total price in cart
    def calculate_total(self) -> float:
        """Calculate total price of all products in cart"""
        total = 0
        for product in self._products:
            total += product.price
        return total
    
    # Responsibility 2: Violating SRP - Prints invoice (Should be in a separate class)
    def print_invoice(self):
        """Print invoice (violates SRP)"""
        print("Shopping Cart Invoice:")
        for product in self._products:
            print(f"{product.name} - Rs {product.price}")
        print(f"Total: Rs {self.calculate_total()}")
    
    # Responsibility 3: Violating SRP - Saves to DB (Should be in a separate class)
    def save_to_database(self):
        """Save cart to database (violates SRP)"""
        print("Saving shopping cart to database...")


# Main execution
if __name__ == "__main__":
    cart = ShoppingCart()
    
    # Creating products
    laptop = Product("Laptop", 50000)
    mouse = Product("Mouse", 2000)
    
    # Adding products to cart
    cart.add_product(laptop)
    cart.add_product(mouse)
    
    # Violating SRP - same class handling multiple responsibilities
    cart.print_invoice()
    cart.save_to_database()