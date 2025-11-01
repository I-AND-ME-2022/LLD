


from vehicle.bike import Bike
from vehicle.car import Car


class VehicleFactory:
    
    def createVehicle(license_num:str,vehicle_type:int):
        
        if vehicle_type == 1:
            return Car(license_num)
        elif vehicle_type == 2:
            return Bike(license_num)
        else:
            raise ValueError("Invalid type")
    