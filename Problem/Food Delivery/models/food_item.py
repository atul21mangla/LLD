class FoodItem:

    def __init__(self,code:str,name:str,price:float):

        self.__code = code
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.__code} : {self.name} : Rs.{self.price}"
    
    def __repr__(self):
        return self.__str__()

    def get_code(self):
        return self.__code
    
    
