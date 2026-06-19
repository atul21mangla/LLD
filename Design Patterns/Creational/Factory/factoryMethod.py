from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def get_vehicle(self):
        pass


class Car(Vehicle):

    def drive(self):
        print("Driving a Car.")

    def get_vehicle(self):
        return "Car"
    
class Bike(Vehicle):

    def drive(self):
        print("Driving a Bike")

    def get_vehicle(self):
        return "Bike"
    
class Truck(Vehicle):

    def drive(self):
        print("Driving a Truck")

    def get_vehicle(self):
        return "Truck"


# Abstract Creator
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass
    
    def deliver_vehicle(self):
        vehicle = self.create_vehicle()
        return f"Delivering: {vehicle.get_vehicle()} - {vehicle.drive()}"

# Concrete Creators
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()

class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        return Truck()
    

def main():
    # Creating vehicles using Factory Method
    car_factory = CarFactory()
    bike_factory = BikeFactory()
    truck_factory = TruckFactory()
    
    print(car_factory.deliver_vehicle())
    print(bike_factory.deliver_vehicle())
    print(truck_factory.deliver_vehicle())

if __name__ == "__main__":
    main()