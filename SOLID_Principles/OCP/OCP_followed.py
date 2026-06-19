
from abc import ABC, abstractmethod


# ==========================
# Product
# ==========================

class Product:
    def __init__(self, name,price):
        self._name = name
        self._price = price
        
    @property
    def name(self):
        return self._name
        
    @property
    def price(self):
        return self._price
        
        
# ==========================
# Shopping Cart
# ==========================

class ShoppingCart():
    
    def __init__(self):
        self.__products = []
        
    def add_product(self,product:Product):
        self.__products.append(product)
        
    @property
    def products(self):
        return self.__products.copy()
        
    def calculate_total(self):
        return sum(p.price for p in self.__products)
        
        
# ==========================
# Invoice Printer
# ==========================

class ShoppingCartInvoice:
    
    def __init__(self,cart:ShoppingCart):
        self.__cart = cart
        
    def printInvoice(self):
        print("\n========== SHOPPING CART INVOICE ==========")

        for product in self.__cart.products:
            print(
                f"Product: {product.name:<10} "
                f"Price: Rs {product.price}"
            )

        print("-------------------------------------------")
        print(f"Total Amount: Rs {self.__cart.calculate_total()}")
        print("===========================================\n")
        
        
# ==========================
# Storage Abstraction
# ==========================

class Storage(ABC):
    
    @abstractmethod
    def save(self, cart: ShoppingCart):
        pass
        
        
# ==========================
# SQL Storage
# ==========================
class SQLStorage(Storage):

    def save(self, cart: ShoppingCart):
        print("Saving to SQL Database...")
        print(f"Total Amount: Rs {cart.calculate_total()}")
        print("SQL Query: INSERT INTO orders VALUES (...)\n")


# ==========================
# NoSQL Storage
# ==========================
class NoSQLStorage(Storage):

    def save(self, cart: ShoppingCart):
        print("Saving to NoSQL Database...")
        print(f"Total Amount: Rs {cart.calculate_total()}")
        print("NoSQL Query: db.orders.insert({...})\n")


# ==========================
# CSV Storage
# ==========================
class CSVStorage(Storage):

    def save(self, cart: ShoppingCart):
        print("Saving to CSV File...")
        print(f"Total Amount: Rs {cart.calculate_total()}")
        print("Writing to orders.csv\n")


# ==========================
# JSON Storage
# ==========================
class JSONStorage(Storage):

    def save(self, cart: ShoppingCart):
        print("Saving to JSON File...")
        print(f"Total Amount: Rs {cart.calculate_total()}")
        print("Writing to orders.json\n")        
        
        
class ShoppingCartStorage:
    
    def __init__(self, cart:ShoppingCart, storage:Storage):
        self.__cart = cart
        self.__storage = storage
        
    def save(self):
        self.__storage.save(self.__cart)
        
    
# ==========================
# Client Code
# ==========================
if __name__ == "__main__":

    product1 = Product("Apple", 20)
    product2 = Product("Mango", 45)
    product3 = Product("Banana", 15)

    cart = ShoppingCart()

    cart.add_product(product1)
    cart.add_product(product2)
    cart.add_product(product3)

    print(f"Cart Total = Rs {cart.calculate_total()}")

    # Invoice
    invoice = ShoppingCartInvoice(cart)
    invoice.printInvoice()

    # Save to SQL
    sql_storage = ShoppingCartStorage(
        cart,
        SQLStorage()
    )
    sql_storage.save()

    # Save to NoSQL
    nosql_storage = ShoppingCartStorage(
        cart,
        NoSQLStorage()
    )
    nosql_storage.save()

    # Save to CSV
    csv_storage = ShoppingCartStorage(
        cart,
        CSVStorage()
    )
    csv_storage.save()
    
    