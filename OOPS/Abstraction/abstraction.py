# Abstraction hides unnecessary details from a client, 
# and showcases only whats is necessary.

from abc import ABC, abstractmethod

"""
Abstract class --> 
1. Act as an interface for the outside world to operate the car. 
2. This abstract class tells 'WHAT' all it can do rather then 'HOW' it does that.
3. Since this is an abstract class we cannot directly create Objects of this class. 
4. We need to Inherit it first and then that child class will have the responsibility to 
provide implementation details of all the abstract (virtual) methods in the class.

5. In our real world example of Car, imagine you sitting in the car and able to operate
the car (startEngine, accelerate, brake, turn) just by pressing or moving some
pedals/buttons/ steer the wheel etc. You dont need to know how these things work, and
also they are hidden under the hood.
6. This Class 'Car' denotes that (pedals/buttons/steering wheel etc). 
"""
class Car(ABC):
    @abstractmethod
    def startEngine(self):
        pass
    
    @abstractmethod
    def shiftGear(self, gear):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass
    
    @abstractmethod
    def brake(self):
        pass
    
    @abstractmethod
    def stopEngine(self):
        pass

"""
1. This is a Concrete class (A class that provide implementation details of an abstract class).
Now anyone can make an Object of 'SportsCar' and can assign it to 'Car' (Parent class) reference
(See main method for this)

2. In our real world example of Car, as you cannot have a real car by just having its body only
(all these buttons or steering wheel). You need to have the actual implementation of 'What' happens
when we press these buttons. 'SportsCar' class denotes that actual implementation. 

3. Therefore, to denote a real world car in programming we created 2 classes.
One to denote all the user-interface like pedals, buttons, steering wheels etc ('Car' class). And,
Another one to denote the actual car with all the implementations of these buttons (SportsCar' class).
 
"""
class SportsCar(Car):
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.isEngineOn = False
        self.currentSpeed = 0
        self.currentGear = 0
    
    def startEngine(self):
        self.isEngineOn = True
        print(f"{self.brand} {self.model} : Engine starts with a roar!")
    
    def shiftGear(self, gear: int):
        if not self.isEngineOn:
            print(f"{self.brand} {self.model} : Engine is off! Cannot Shift Gear.")
            return
        self.currentGear = gear
        print(f"{self.brand} {self.model} : Shifted to gear {self.currentGear}")
    
    def accelerate(self):
        if not self.isEngineOn:
            print(f"{self.brand} {self.model} : Engine is off! Cannot accelerate.")
            return
        self.currentSpeed += 20
        print(f"{self.brand} {self.model} : Accelerating to {self.currentSpeed} km/h")
    
    def brake(self):
        self.currentSpeed -= 20
        if self.currentSpeed < 0:
            self.currentSpeed = 0
        print(f"{self.brand} {self.model} : Braking! Speed is now {self.currentSpeed} km/h")
    
    def stopEngine(self):
        self.isEngineOn = False
        self.currentGear = 0
        self.currentSpeed = 0
        print(f"{self.brand} {self.model} : Engine turned off.")

# Main Method
if __name__ == "__main__":
    myCar: Car = SportsCar("Ford", "Mustang")
    
    myCar.startEngine()
    myCar.shiftGear(1)
    myCar.accelerate()
    myCar.shiftGear(2)
    myCar.accelerate()
    myCar.brake()
    myCar.stopEngine()