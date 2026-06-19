"""
Encapsulation says 2 things:
1. An Object's Characteristics and its behaviour are encapsulated together
within that Object.
2. All the characteristics or behaviours are not for everyone to access.
Object should provide data security.

We follow above 2 pointers about Object of real world in programming by:
1. Creating a class that act as a blueprint for Object creation. Class contain
all the characteristics (class variable) and behaviour (class methods) in one block,
encapsulating it together.
2. We introduce access modifiers (public, private, protected) etc to provide data
security to the class members.
"""
class SportsCar:
    def __init__(self, brand: str, model: str):
        # Private attributes (using double underscore for name mangling)
        # In Python, there's no true private like C++, but by convention:
        # - Single underscore _ indicates "protected" (internal use)
        # - Double underscore __ indicates "private" (name mangling)
        self.__brand = brand
        self.__model = model
        self.__isEngineOn = False
        self.__currentSpeed = 0
        self.__currentGear = 0
        
        # Introduce new variable to explain setters/getters
        self.__tyreCompany = "MRF"
    
    # Getter methods
    def getSpeed(self) -> int:
        return self.__currentSpeed
    
    def getTyreCompany(self) -> str:
        return self.__tyreCompany
    
    # Setter method
    def setTyreCompany(self, tyreCompany: str):
        self.__tyreCompany = tyreCompany
    
    # Alternative Pythonic way using @property decorator (more Pythonic than getters/setters)
    @property
    def speed(self) -> int:
        """Pythonic property - alternative to getSpeed()"""
        return self.__currentSpeed
    
    @property
    def tyre_company(self) -> str:
        """Pythonic property getter"""
        return self.__tyreCompany
    
    @tyre_company.setter
    def tyre_company(self, value: str):
        """Pythonic property setter"""
        self.__tyreCompany = value
    
    def startEngine(self):
        self.__isEngineOn = True
        print(f"{self.__brand} {self.__model} : Engine starts with a roar!")
    
    def shiftGear(self, gear: int):
        if not self.__isEngineOn:
            print(f"{self.__brand} {self.__model} : Engine is off! Cannot Shift Gear.")
            return
        self.__currentGear = gear
        print(f"{self.__brand} {self.__model} : Shifted to gear {self.__currentGear}")
    
    def accelerate(self):
        if not self.__isEngineOn:
            print(f"{self.__brand} {self.__model} : Engine is off! Cannot accelerate.")
            return
        self.__currentSpeed += 20
        print(f"{self.__brand} {self.__model} : Accelerating to {self.__currentSpeed} km/h")
    
    def brake(self):
        self.__currentSpeed -= 20
        if self.__currentSpeed < 0:
            self.__currentSpeed = 0
        print(f"{self.__brand} {self.__model} : Braking! Speed is now {self.__currentSpeed} km/h")
    
    def stopEngine(self):
        self.__isEngineOn = False
        self.__currentGear = 0
        self.__currentSpeed = 0
        print(f"{self.__brand} {self.__model} : Engine turned off.")


# Main Method
if __name__ == "__main__":
    mySportsCar = SportsCar("Ford", "Mustang")
    
    mySportsCar.startEngine()
    mySportsCar.shiftGear(1)
    mySportsCar.accelerate()
    mySportsCar.shiftGear(2)
    mySportsCar.accelerate()
    mySportsCar.brake()
    mySportsCar.stopEngine()
    
    # # Trying to set arbitrary value to speed - This will NOT work because __currentSpeed is private
    # # Uncommenting the line below will raise an AttributeError
    # # mySportsCar.__currentSpeed = 500  # This creates a NEW attribute, doesn't modify the private one
    
    # print(f"Current Speed of My Sports Car is set to {mySportsCar.__currentSpeed}")  # This would fail
    
    # Using getter method
    print(f"Current Speed of My Sports Car is {mySportsCar.getSpeed()}")
    
    # Using Pythonic property (more elegant)
    # print(f"Current Speed using property: {mySportsCar.speed}")
    
    # The object will be automatically garbage collected when the program ends
    # No need for explicit delete