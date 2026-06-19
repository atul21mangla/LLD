"""
Polymorphism in Python:
1. Dynamic Polymorphism (Method Overriding) - Same method name, different implementations in child classes
2. Static Polymorphism (Method Overloading) - Same method name, different parameters
   Note: Python doesn't support method overloading directly, but we can achieve it using default parameters or variable arguments
"""

from abc import ABC, abstractmethod

# Base Car class
class Car(ABC):
    def __init__(self, brand: str, model: str):
        self._brand = brand
        self._model = model
        self._isEngineOn = False
        self._currentSpeed = 0
    
    # Common methods for all cars
    def startEngine(self):
        self._isEngineOn = True
        print(f"{self._brand} {self._model} : Engine started.")
    
    def stopEngine(self):
        self._isEngineOn = False
        self._currentSpeed = 0
        print(f"{self._brand} {self._model} : Engine turned off.")
    
    # Abstract methods for Dynamic Polymorphism
    @abstractmethod
    def accelerate(self, speed: int = None):
        """Abstract method - can be called with or without speed parameter"""
        pass
    
    @abstractmethod
    def brake(self):
        pass


class ManualCar(Car):
    def __init__(self, brand: str, model: str):
        super().__init__(brand, model)
        self._currentGear = 0
    
    # Specialized method for Manual Car
    def shiftGear(self, gear: int):
        self._currentGear = gear
        print(f"{self._brand} {self._model} : Shifted to gear {self._currentGear}")
    
    # Overriding accelerate - Dynamic Polymorphism
    # Achieving method overloading using default parameter
    def accelerate(self, speed: int = None):
        if not self._isEngineOn:
            print(f"{self._brand} {self._model} : Cannot accelerate! Engine is off.")
            return
        
        # If speed parameter is provided (overloaded version), use it
        if speed is not None:
            self._currentSpeed += speed
            print(f"{self._brand} {self._model} : Accelerating to {self._currentSpeed} km/h")
        else:
            # Default acceleration
            self._currentSpeed += 20
            print(f"{self._brand} {self._model} : Accelerating to {self._currentSpeed} km/h")
    
    # Overriding brake - Dynamic Polymorphism
    def brake(self):
        self._currentSpeed -= 20
        if self._currentSpeed < 0:
            self._currentSpeed = 0
        print(f"{self._brand} {self._model} : Braking! Speed is now {self._currentSpeed} km/h")


class ElectricCar(Car):
    def __init__(self, brand: str, model: str):
        super().__init__(brand, model)
        self._batteryLevel = 100
    
    # Specialized method for Electric Car
    def chargeBattery(self):
        self._batteryLevel = 100
        print(f"{self._brand} {self._model} : Battery fully charged!")
    
    # Overriding accelerate - Dynamic Polymorphism
    # Achieving method overloading using default parameter
    def accelerate(self, speed: int = None):
        if not self._isEngineOn:
            print(f"{self._brand} {self._model} : Cannot accelerate! Engine is off.")
            return
        
        if self._batteryLevel <= 0:
            print(f"{self._brand} {self._model} : Battery dead! Cannot accelerate.")
            return
        
        # If speed parameter is provided (overloaded version), use it
        if speed is not None:
            self._batteryLevel -= (10 + speed // 10)  # Reduce battery based on speed
            self._currentSpeed += speed
            print(f"{self._brand} {self._model} : Accelerating to {self._currentSpeed} km/h. Battery at {self._batteryLevel}%.")
        else:
            # Default acceleration
            self._batteryLevel -= 10
            self._currentSpeed += 15
            print(f"{self._brand} {self._model} : Accelerating to {self._currentSpeed} km/h. Battery at {self._batteryLevel}%.")
    
    # Overriding brake - Dynamic Polymorphism
    def brake(self):
        self._currentSpeed -= 15
        if self._currentSpeed < 0:
            self._currentSpeed = 0
        print(f"{self._brand} {self._model} : Regenerative braking! Speed is now {self._currentSpeed} km/h. Battery at {self._batteryLevel}%.")


# Alternative approach: Using @overload from typing module (Python 3.8+)
# This is for type hints only, not actual runtime overloading
"""
from typing import overload

class ManualCar(Car):
    @overload
    def accelerate(self) -> None:
        ...
    
    @overload
    def accelerate(self, speed: int) -> None:
        ...
    
    def accelerate(self, speed: int = None):
        # Same implementation as above
        pass
"""


# Main function
if __name__ == "__main__":
    # Using base class pointers (references) for polymorphism
    myManualCar: Car = ManualCar("Ford", "Mustang")
    myManualCar.startEngine()
    myManualCar.accelerate()      # Calls ManualCar's accelerate (no parameter)
    myManualCar.accelerate()      # Calls ManualCar's accelerate again
    myManualCar.brake()
    myManualCar.stopEngine()
    
    print("----------------------")
    
    myElectricCar: Car = ElectricCar("Tesla", "Model S")
    myElectricCar.startEngine()
    myElectricCar.accelerate()    # Calls ElectricCar's accelerate (no parameter)
    myElectricCar.accelerate()    # Calls ElectricCar's accelerate again
    myElectricCar.brake()
    myElectricCar.stopEngine()
    
    # Example of using overloaded accelerate (with speed parameter)
    print("\n--- Demonstrating overloaded accelerate with speed parameter ---")
    myManualCar2 = ManualCar("Ferrari", "488 GTB")
    myManualCar2.startEngine()
    myManualCar2.accelerate(50)   # Calls overloaded version with speed parameter
    myManualCar2.brake()
    myManualCar2.stopEngine()
    
    # No need for explicit delete - automatic garbage collection