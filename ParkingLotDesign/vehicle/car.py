
from vehicle.vehicle import Vehicle
from vehicle.vehicle_type import VehicleType

class Car(Vehicle):
    
    def __init__(self, license_num:str):
        super().__init__(license_num,VehicleType.CAR)
