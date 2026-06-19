class Car:
    def __init__(self, brand: str, model: str):
        # Protected attributes (convention: single underscore for internal use)
        self._brand = brand
        self._model = model
        self._isEngineOn = False
        self._currentSpeed = 0
    
    # Common methods for All cars
    def startEngine(self):
        self._isEngineOn = True
        print(f"{self._brand} {self._model} : Engine started.")
    
    def stopEngine(self):
        self._isEngineOn = False
        self._currentSpeed = 0
        print(f"{self._brand} {self._model} : Engine turned off.")
    
    def accelerate(self):
        if not self._isEngineOn:
            print(f"{self._brand} {self._model} : Cannot accelerate! Engine is off.")
            return
        self._currentSpeed += 20
        print(f"{self._brand} {self._model} : Accelerating to {self._currentSpeed} km/h")
    
    def brake(self):
        self._currentSpeed -= 20
        if self._currentSpeed < 0:
            self._currentSpeed = 0
        print(f"{self._brand} {self._model} : Braking! Speed is now {self._currentSpeed} km/h")


class ManualCar(Car):  # Inherits from Car
    def __init__(self, brand: str, model: str):
        # Call parent class constructor
        super().__init__(brand, model)
        self._currentGear = 0  # specific to Manual Car
    
    # Specialized method for Manual Car
    def shiftGear(self, gear: int):
        self._currentGear = gear
        print(f"{self._brand} {self._model} : Shifted to gear {self._currentGear}")


class ElectricCar(Car):  # Inherits from Car
    def __init__(self, brand: str, model: str):
        # Call parent class constructor
        super().__init__(brand, model)
        self._batteryLevel = 100  # specific to Electric Car
    
    # Specialized method for Electric Car
    def chargeBattery(self):
        self._batteryLevel = 100
        print(f"{self._brand} {self._model} : Battery fully charged!")


# Main Method
if __name__ == "__main__":
    myManualCar = ManualCar("Suzuki", "WagonR")
    myManualCar.startEngine()
    myManualCar.shiftGear(1)  # specific to manual car
    myManualCar.accelerate()
    myManualCar.brake()
    myManualCar.stopEngine()
    # No need for delete - automatic garbage collection

    print("----------------------")

    myElectricCar = ElectricCar("Tesla", "Model S")
    myElectricCar.chargeBattery()  # specific to electric car
    myElectricCar.startEngine()
    myElectricCar.accelerate()
    myElectricCar.brake()
    myElectricCar.stopEngine()
    # No need for delete - automatic garbage collection

