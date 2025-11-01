from vehicle.vehicle import Vehicle
from vehicle.vehicle_type import VehicleType
class Bike(Vehicle):
    
    def __init__(self, license_num:str):
        super().__init__(license_num,VehicleType.BIKE)