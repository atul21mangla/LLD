from abc import ABC, abstractmethod

# Abstract Products
class Engine(ABC):
    @abstractmethod
    def get_engine_type(self):
        pass

class Wheels(ABC):
    @abstractmethod
    def get_wheel_count(self):
        pass

# Concrete Products for Car
class CarEngine(Engine):
    def get_engine_type(self):
        return "V8 Engine"

class CarWheels(Wheels):
    def get_wheel_count(self):
        return 4

# Concrete Products for Bike
class BikeEngine(Engine):
    def get_engine_type(self):
        return "2-Stroke Engine"

class BikeWheels(Wheels):
    def get_wheel_count(self):
        return 2

# Concrete Products for Truck
class TruckEngine(Engine):
    def get_engine_type(self):
        return "Diesel Engine"

class TruckWheels(Wheels):
    def get_wheel_count(self):
        return 8

# Abstract Factory
class VehiclePartsFactory(ABC):
    @abstractmethod
    def create_engine(self):
        pass
    
    @abstractmethod
    def create_wheels(self):
        pass

# Concrete Factories
class CarPartsFactory(VehiclePartsFactory):
    def create_engine(self):
        return CarEngine()
    
    def create_wheels(self):
        return CarWheels()

class BikePartsFactory(VehiclePartsFactory):
    def create_engine(self):
        return BikeEngine()
    
    def create_wheels(self):
        return BikeWheels()

class TruckPartsFactory(VehiclePartsFactory):
    def create_engine(self):
        return TruckEngine()
    
    def create_wheels(self):
        return TruckWheels()
    

def main():
    def build_vehicle(parts_factory):
        engine = parts_factory.create_engine()
        wheels = parts_factory.create_wheels()
        return f"Vehicle built with: {engine.get_engine_type()} and {wheels.get_wheel_count()} wheels"
    
    car_parts = CarPartsFactory()
    bike_parts = BikePartsFactory()
    truck_parts = TruckPartsFactory()
    
    print("Car:", build_vehicle(car_parts))
    print("Bike:", build_vehicle(bike_parts))
    print("Truck:", build_vehicle(truck_parts))

if __name__ == "__main__":
    main()