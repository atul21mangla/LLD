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
    


# Vehicle Factory

class VehicleFactory():

    def create_vehicle(self,vehicle_type:str):

        if vehicle_type == "Car":
            return Car()
        
        elif vehicle_type == "Bike":
            return Bike()
        elif vehicle_type == "Truck":
            return Truck()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
        

def main():
    factory = VehicleFactory()
    vehicle = factory.create_vehicle("Bike")
    vehicle.drive()
    print(vehicle.get_vehicle())


if __name__ == "__main__":
    main()
    
