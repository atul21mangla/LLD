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
        
        
class ShoppingCartInvoice:
    
    def __init__(self,cart:ShoppingCart):
        self.__cart = cart
        
    def printInvoice(self):
        print("Shopping Cart Invoice:\n")
        p = self.__cart.products
        for x in p:
            print(f"Product name - {x.name}\nProduct Price - {x.price}")
        
class ShoppingCartStorage:
    
    def __init__(self, cart:ShoppingCart):
        self.__cart = cart
        
    # VIOLATION: Adding a new storage type requires modifying this method
    def save_to_database(self, storage_type: str):
        if storage_type == "SQL":
            self._save_to_sql()
        elif storage_type == "NoSQL":
            self._save_to_nosql()
        elif storage_type == "CSV":
            self._save_to_csv()  # New requirement - must modify existing code!
        elif storage_type == "JSON":
            self._save_to_json()  # Another new requirement - more modification!
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")
    
    def _save_to_sql(self):
        print("Saving to SQL Database...")
        print(f"  - Total amount: Rs {self.__cart.calculate_total()}")
        print("  - SQL: INSERT INTO orders VALUES (...)")
    
    def _save_to_nosql(self):
        print("Saving to NoSQL Database...")
        print(f"  - Total amount: Rs {self.__cart.calculate_total()}")
        print("  - NoSQL: db.orders.insert({...})")
    
    # New requirement - must add new methods and modify above logic
    def _save_to_csv(self):
        print("Saving to CSV File...")
        print(f"  - Total amount: Rs {self.__cart.calculate_total()}")
        print("  - CSV: writing to orders.csv")
    
    def _save_to_json(self):
        print("Saving to JSON File...")
        print(f"  - Total amount: Rs {self.__cart.calculate_total()}")
        print("  - JSON: writing to orders.json")
        
    
if __name__ == "__main__":
    product1 = Product("Apple",20)
    product2 = Product("Mango",45)
    
    shoppingcart = ShoppingCart()
    shoppingcart.add_product(product1)
    shoppingcart.add_product(product2)
    
    total = shoppingcart.calculate_total()
    print(f"Cart Total : {total}")
    
    cart_invoice = ShoppingCartInvoice(shoppingcart)
    
    cart_invoice.printInvoice()
    
    cart_storage = ShoppingCartStorage(shoppingcart)
    
    cart_storage.save_to_database("NoSQL")
    
    